from rest_framework import permissions
from django.contrib.auth.models import Permission
from accounts.models import User_Groupes, Groupe_Permissions

def check_permission(user, method, permission_to):
    if not user.user.is_authenticated:
        return False
    if user.is_owner:
        return True
    required_permission = '_view_' + permission_to
    if method == 'POST':
        required_permission = 'add_' + permission_to
    elif method == 'PUT':
        required_permission = 'change_' + permission_to
    elif method == 'DELETE':
        required_permission = 'delete_' + permission_to

    groups = User_Groupes.objects.values('group_id').filter(user_id=user.user.id).all()
    
    for group in groups:
        permissions = Groupe_Permissions.objects.values('permission_id').filter(group_id=group['group_id']).all()
        
        for permission in permissions:
            if Permission.objects.filter(id=permission['permission_id'], codename=required_permission).exists():
                return True

class EmployeesPermission(permissions.BasePermission):
   message = 'You do not have permission to manage employees'
   def has_permission(self, request, _view):
       return check_permission(request.user, request.method, permission_to='employee')

class GroupesPermission(permissions.BasePermission):
   message = 'You do not have permission to manage groupes'
   def has_permission(self, request, _view):
       return check_permission(request.user, request.method, permission_to='group')    

class GroupsPermissionsPermission(permissions.BasePermission):
   message = 'You do not have permission to manage permissions'
   def has_permission(self, request, _view):
       return check_permission(request.user, request.method, permission_to='permission')

class TaskPermission(permissions.BasePermission):
   message = 'You do not have permission to manage employees tasks' 
   def has_permission(self, request, _view):
       return check_permission(request.user, request.method, permission_to='task')