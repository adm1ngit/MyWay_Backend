from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models

#------Jarimalar YHQ START-------------#
class JarimaBandi(models.Model):
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
    band = models.ManyToManyField(JarimaBandi)
    def __str__(self):
        return self.name2
#------Jarimalar YHQ END --------------#

# -------- YHQ Qoidalar START-----------------#
class YHQQoidalar(models.Model):
    title = models.CharField(max_length=300)
    def __str__(self):
        return self.title
class YHQQoidalarCategory(models.Model):
    name = models.CharField(max_length=300)
    YHQQoidalar = models.ForeignKey(YHQQoidalar, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class YHQQoida(models.Model):
    text = models.TextField()
    img = models.ImageField(upload_to='belgilar/photos', blank=True, null=True)
    category = models.ForeignKey(YHQQoidalarCategory, on_delete=models.CASCADE)

# -------- YHQ Qoidalar END -----------------#

#---------- Manzillar START------------------------#
class addresses(models.Model):
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    location = models.CharField(max_length=250)


#---------- Manzillar END------------------------#