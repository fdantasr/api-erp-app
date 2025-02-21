from companies.views.base import Base
from companies.utils.permissions import EmployeesPermission, Group_Permissions
from companies.models import Employee, Enterprise
from companies.serializers import EmployeesSerializer, EmployeeSerializer 

from accounts.auth import Authentication
from accounts.models import User, User_Groups

from rest_framework.views import Response, status
from rest_framework.exceptions import APIException

class Employees(Base):
    permission_classes = [EmployeesPermission]
    
    def get(self, request):
        enterprise_id = self.get_enterprise_id(request.user.id)
    #Get owner of enterprise
        owner_id = Enterprise.objects.values('user_id').filter(id=enterprise_id).first()['user_id']
    #Get all employees of enterprise except owner
        employees = Employee.objects.filter(enterprise_id=enterprise_id).exclude(user_id=owner_id).all()
        
        serializer = EmployeesSerializer(employees, many=True)
       
        return Response({
            'employees': serializer.data
        })
    
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        enterprise_id = self.get_enterprise_id(request.user.id)
        signup_user = Authentication.signup(self, name=name, email=email, password=password, type_account='employee', company_id=enterprise_id)
        
        if isinstance(signup_user, User):
            return Response({
                'success': True,
                'message': 'Employee created successfully'
            }, status=status.HTTP_201_CREATED)
        return Response(signup_user, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetail(Base):
    permission_classes = [EmployeesPermission]
    
    def get(self, request, employee_id):
        employee = self.get_employee(request.user.id, employee_id)
        
        serializer = EmployeeSerializer(employee)
        
        return Response({
            'employee': serializer.data
        })
    
    def put(self, request, employee_id):
        groups = request.data.get('groups')
        employee = self.get_employee(request.user.id, employee_id)
        
        name = request.data.get('name') or employee.user.name
        email = request.data.get('email') or employee.user.email
        
        if email != employee.user.email and User.objects.filter(email=email).exists():
            raise APIException('Email already exists', code="email_already_used")
        
        User.objects.filter(id=employee.user.id).update(name=name, email=email) #update no user a partir do funcionário encontrado
        
        User_Groups.objects.filter(user_id=employee.user.id).delete()
        if groups:
            #Transformou a string de grupos em uma lista de grupos 1,2,3 -> [1,2,3]
            groups = groups.split(',')
            for group_id in groups:
                self.get_group(group_id, employee.enterprise_id)
                User_Groups.objects.create(user_id=employee.user.id, group_id=group_id)
            return Response({
                'success': True,
                'message': 'Employee updated successfully'
            })

    def delete(self, request, employee_id):
        employee = self.get_employee(request.user.id, employee_id)
    
        check_if_owner = User.objects.filter(id=employee.user.id, is_ower=1).exists()
        if check_if_owner:
            raise APIException('You cannot delete the owner of the company', code="owner_cannot_delete")
        
        employee.delete()
        #Um usuário não necessariamente é um funcionário, então é necessário deletar o usuário também
        User.objects.filter(id=employee.user.id).delete() 
        
        return Response({
                'success': True,
                'message': 'Employee deleted successfully'
            })