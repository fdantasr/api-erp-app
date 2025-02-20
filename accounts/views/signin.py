from accounts.views.base import Base
from accounts.auth import Authentication

class SignIn(Base):
    def post(self, request):
      email = request.data.get('email')
      password = request.data.get('password')