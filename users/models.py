from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'customer', 'Customer'
        MANAGER = 'manager', 'Manager'
        ADMIN = 'admin', 'Admin'
        
    role = models.CharField(max_length=20,choices=Role.choices,default=Role.CUSTOMER)
    
    def __str__(self):
        return self.username
    
    