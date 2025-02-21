from accounts.auth import Authentication
from accounts.serializers import UserSerializer
from accounts.views.base import Base
from rest_framework.response import Response

class SignUp(Base):   
    def post(self, request) -> None:
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = Authentication().signup(name=name, email=email, password=password)
    
        serializer = UserSerializer(user)
        return Response({
        "user": serializer.data
        })
    