from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=11, null=True)
    address = models.TextField(null=True)
    birth_date=models.DateField(null=True)
    major_bank = models.TextField(null=True)

