from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
# Create your models here.
class Signup(models.Model):
    objects=UserManager()
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    Email=models.CharField(max_length=100)
    # roll_number=models.CharField(max_length=300)
    Password=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    def __str__(self):
        return self.username
