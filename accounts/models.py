from django.db import models
from django.contrib.auth.models import AbstractBaseUser, Permission
from companies.models import Enterprise

# Create your models here.

class User(AbstractBaseUser):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True) #time int no SQL
    USERNAME_FIELD = 'email'
    def __str__(self) -> str:
        return self.email

class Groupe(models.Model): #Um Grupo é um cargo
    name = models.CharField(max_length=85)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)

class Groupe_Permissions(models.Model):
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class User_Groups(models.Model): #em quais grupos o usuário está
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    groupe = models.ForeignKey(Groupe, on_delete=models.CASCADE)