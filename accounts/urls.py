from accounts.views.signin import SignIn
from accounts.views.signup import SignUp
from accounts.views.user import GetUser

from django.urls import path

urlpatterns = [
    path('signin/', SignIn.as_view()),  
    path('signup/', SignUp.as_view()),
    path('user/', GetUser.as_view())
]