from django.db import models

# Create your models here.
class UserModel(models.Model):
    NameF=models.CharField(max_length=255)
    EmailF=models.CharField(max_length=255)
    PasswordF=models.CharField(max_length=255)
    DateF=models.DateField(auto_now=True)
    TimeF=models.TimeField(auto_now=True)