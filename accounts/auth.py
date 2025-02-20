from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:

    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed('Email e/ou senha incorreto(s)')
        
        # Verificando se o usuário existe
        user = User.objects.filter(email=email).first()

        if not user:
            raise exception_auth
        
        # Verificando a senha
        if not check_password(password, user.password):
            raise exception_auth 
        
        return user
    
    def signup(self, name, email, password, type_account="owner", company_id=False):
        # Validações dos campos 
        if not name or name == '':
            raise APIException('Nome não pode ser Null')
        if not email or email == '':
            raise APIException('Email não pode ser Null')
        if not password or password == '':
            raise APIException('Password não pode ser Null')
        if type_account == 'employee' and not company_id:
            raise APIException('ID da empresa não pode ser Null')
        
        # Verificando se o email já está cadastrado
        if User.objects.filter(email=email).exists():
            raise APIException('Email já cadastrado')
        
        # Criptografando a senha
        password_hashed = make_password(password)

        # Criando o usuário
        created_user = User.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        # Criando a empresa se for o owner
        if type_account == 'owner':
            created_enterprise = Enterprise.objects.create(
                name="Nome da empresa",  
                user_id=created_user.id
            )
        
        # Criando o funcionário se for o employee
        if type_account == 'employee':
            Employee.objects.create(
                user_id=created_user.id,
                enterprise_id=company_id or created_enterprise.id
            )

        return created_user
