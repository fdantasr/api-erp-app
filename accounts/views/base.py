from rest_framework.views import APIView
from companies.models import Enterprise
from rest_framework.exceptions import APIException
from accounts.models import User_Groupe

class Base(APIView):
    def get_enterprise_user(self, user_id) -> dict[str, any] | None:
        enterprise = {
            "is_owner": False,
            "permissions": []
        }
        
        enterprise["is_owner"] = Enterprise.objects.filter(user_id=user_id).exists()
        
        if enterprise["is_owner"]: return enterprise

        #Permissions Get Employee

        employee = Enterprise.objects.filter(user_id=user_id).first()

        if not employee: raise APIException('Este usuário não é um funcionário')

        groups = User_Groupe.objects.filter(user_id=user_id).all()
        
        for g in groups:
           group = g.group
           permissions = User_Groupe.objects.filter(group=group).all()
           for p in permissions:
               enterprise["permissions"].append({
                   "id": p.permission.id,
                   "label": p.permission.name, 
                   "codename": p.permission.codename
               })
        return enterprise
