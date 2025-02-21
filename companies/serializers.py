from rest_framework import serializers

from companies.models import Employee, Task
from accounts.models import User, User_Groups, Group, Group_Permissions
from django.contrib.auth.models import Permission

class EmployeesSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField() 
    email = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email'
        )
        
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email
    
class EmployeeSerializer(serializers.ModelSerializer):
    
    name = serializers.SerializerMethodField() 
    email = serializers.SerializerMethodField()
    groups = serializers.SerializerMethodField()
    
    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'email',
            'groups'
        )
        
    def get_name(self, obj):
        return obj.user.name
    
    def get_email(self, obj):
        return obj.user.email
    
    def get_groups(self, obj):
        groupsDB = User_Groups.objects.filter(user_id=obj.user.id).all()
        groupsData = []
        for group in groupsDB:
            groupsData.append({
                'id': group.group.id,
                'name': group.group.name
            })
        return groupsData

class GroupSerializer(serializers.ModelSerializer):
    
    permissions = serializers.SerializerMethodField()
    
    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'permissions'
        )
        def get_permissions(self, obj):
           groups = Group_Permissions.objects.filter(group_id=obj.id).all()
           permissions = []
           
           for group in groups:
               permissions.append({
                   'id': group.permission.id,
                   'label': group.permission.name,
                   'codename': group.permission.codename
               })
           return permissions

class PermissionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Permission
        fields = (
            'id',
            'name',
            'codename'
        )

class TasksSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'status',
            'due_date'
            'created_at' 
        )
    def get_status(self, obj):
        return obj.status.name

class TaskSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()
    
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'status',
            'due_date',
            'created_at',
            'employee'
        )
    def get_status(self, obj):
        return obj.status.name

    def get_employee(self, obj):
        return EmployeeSerializer(obj.employee).data
    
    def update(self, instance, validated_data): #Django usa o validated_data para atualizar os dados do objeto no banco de dados
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.status = validated_data.get('status', instance.status)
        instance.employee = validated_data.get('employee', instance.employee)
        instance.save()
        return instance