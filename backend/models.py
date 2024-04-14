from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager

#------Jarimalar YHQ ---------
class Band(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    price_main = models.CharField(max_length=50)  # Store price as an integer
    price_sale30 = models.CharField(max_length=50)  # Sale price with 30% discount (integer)
    price_sale50 = models.CharField(max_length=50)  # Sale price with 50% discount (integer)

class JarimaToifasi(models.Model):
    name1 = models.CharField(max_length=250, unique=True)
    def __str__(self):
        return self.name1

class Jarima(models.Model):
    name2 = models.TextField()
    category = models.ForeignKey(JarimaToifasi, on_delete=models.CASCADE)
    band = models.ManyToManyField(Band)
    def __str__(self):
        return self.name2
#------Jarimalar YHQ END ---------




class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        return self.email

