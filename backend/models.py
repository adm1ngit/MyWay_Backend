from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from shared.models import BaseModel




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




class qoida(models.Model):
    pass

