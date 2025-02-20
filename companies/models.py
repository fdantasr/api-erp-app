from django.db import models

# Create your models here.
class Enterprise(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

class Employee(models.Model):
   user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
   enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)