from rest_framework.exceptions import AuthenticationFailed, APIException
from django.contrib.auth.hashers import check_password, make_password
from accounts.models import User
from companies.models import Enterprise, Employee

class Authentication:

    def signin(self, email=None, password=None) -> User:
        excpetion_auth = AuthenticationFailed('Email e/ou senha incorreto(s)')
        user_exists=User.objects.filter(email=email).exists()

        if not user_exists:
            raise  excpetion_auth
        
        user = User.objects.filter(email=email).first()

        if not check_password(password, user.password):
            raise excpetion_auth 
        return user
    
    def signup(self, name, email, password, type_account="owner", company_id=False):
        #Validações dos campos 
        if not name or name == '':
            raise APIException('Nome não pode ser Null')
        if not email or email == '':
            raise APIException('Email não pode ser Null')
        if not password or password == '':
            raise APIException('Password não pode ser Null')
        if type_account == 'employee' and not company_id:
            raise APIException('ID da empresa não pode ser Null')
            
        user = User
        if user.objects.filter(email=email).exists():
            raise APIException('Email já cadastrado')
        
        #Criptografando a senha
        password_hashed = make_password(password)

        created_user = user.objetcts.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )
        #Criando a empresa 
        if type_account == 'owner':
           created_enterprise = Enterprise.objects.create(
                name="Nome da empresa",
                user_id=created_user.id
            )
        #Criando o funcionário
        if type_account == 'employee':
            Employee.objects.create(
                  user_id=created_user.id,
                  enterprise_id=company_id or created_enterprise.id
            )
        return created_user