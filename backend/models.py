from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models


#---------- Manzillar START ------------------------#
class ServiceAddres(models.Model):
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=250)
    location = models.CharField(max_length=250)


#---------- Manzillar END ------------------------#

#---------- Texnik Ko'rik START -----------------#
class TexServiceOrder(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    avtoNum = models.CharField(max_length=50)
    Date = models.DateField()
    region = models.CharField(max_length=50)
    myService = models.CharField(max_length=150)
    locations = models.ForeignKey(ServiceAddres, on_delete=models.CASCADE)


#---------- Texnik Ko'rik END -----------------#

# ------------ Gas START --------------------#
class Gas(models.Model):
    name = models.CharField(max_length=150)
    startDate = models.DateField()
    endDate = models.DateField()
    testDate = models.DateField()


# ------------ Gas END ----------------------#
#---------------- Car oil START ---------------#
class CarOil(models.Model):
    startDate = models.DateField()
    traveled = models.IntegerField(150)
    brand = models.CharField(max_length=150)
    recommendedKm = models.IntegerField(150)
    dailyKm = models.IntegerField(150)

#---------------- Car oil END ---------------#

#---------------- Ishonchnoma START ----------------------#
class Affidavit(models.Model):
    fName = models.CharField(max_length=150)
    guvoxnomaNum = models.IntegerField(20)
    startDate = models.DateField()
    endDate = models.DateField()
    lifeTime = models.CharField(max_length=150)
    givenName = models.CharField(max_length=150)
    pasSeria = models.CharField(max_length=2, blank=True)
    pasNum = models.IntegerField(6, blank=True)
    guvoxnoma2Num = models.IntegerField(150)

    def __str__(self):
        return self.fName

#---------------- Ishonchnoma END ------------------------#

#---------------- Texnik xizmat ko'rsatish START --------------------#
class TexServiceMessage(models.Model):
    email = models.EmailField(max_length=150)
    phoneNumber = models.IntegerField()
    event = models.CharField(max_length=250)
    def __str__(self):
        return self.email
#---------------- Texnik xizmat ko'rsatish END --------------------#

#---------------- Haydovchilik guvohnomasini tiklash START ----------------#
class RestoreLicense(models.Model):
    fName = models.CharField(max_length=150)
    licenseNumber = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    phoneNum = models.CharField(max_length=150)
    def __str__(self):
        return self.fName


#---------------- Haydovchilik guvohnomasini tiklash END ----------------#

#---------------- Avtotest  START -----------------------------------#
class AutoTest(models.Model):
    trueAnswer = models.IntegerField(default=0)
    falseAnswer = models.IntegerField(default=0)
    fullAnswer = models.IntegerField(default=0)
    testID = models.IntegerField(default=0)
    date = models.DateField()
#---------------- Avtotest  START -----------------------------------#