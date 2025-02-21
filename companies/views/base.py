from rest_framework.views import APIView
from companies.utils.exceptions import NotFoundEmployee, NotFoundGroup, NotFoundTask, NotFoundTaskStatus
from companies.models import Employee, Task, TaskStatus, Enterprise
from accounts.models import Group

#Funções de apoio para as views

class Base(APIView):
    def get_enterprise_id(self, user_id):
        employee = Employee.objects.filter(user_id=user_id).first()
        owner = Enterprise.objects.filter(user_id=user_id).first()
        
        if employee:
            return employee.enterprise_id
     
        return owner.id
    
    def get_employee(self, user_id, employee_id):
       enterprise_id = self.get_enterprise_id(user_id)
       employee = Employee.objects.filter(id=employee_id, enterprise_id=enterprise_id).first()
       
       if not employee:
           raise NotFoundEmployee()
   
    def get_group(self, group_id, enterprise_id):
        group = Group.objects.values('name').filter(id=group_id, enterprise_id=enterprise_id).first()
        
        if not group:
            raise NotFoundGroup()
        return group
    
    def get_status (self, status_id):
        status = TaskStatus.objects.values('name').filter(id=status_id).first()
        
        if not status:
            raise NotFoundTaskStatus()
        return status

    def get_task(self, task_id, enterprise_id):
        task = Task.objects.filter(id=task_id, enterprise_id=enterprise_id).first()
        
        if not task:
            raise NotFoundTask()
        return task