from django.db import models
import random
import string

class addCar(models.Model):
    userName = models.CharField(max_length=150)
    email = models.EmailField()
    carNamber = models.CharField(max_length=10)
    texSeries = models.CharField(max_length=10)
    texNum = models.CharField(max_length=10)
    avtoMark = models.CharField(max_length=20)
    avtoName = models.CharField(max_length=20)
    avtoYear = models.IntegerField()
    avtoEngine = models.CharField(max_length=50)
    avtoColor = models.CharField(max_length=50)
    docNumber = models.IntegerField()
    docDate = models.DateField()
    politicalNum = models.CharField(max_length=150)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    avtoBuyDate = models.DateField()
    avtoPrice = models.CharField(max_length=150)
    avtoCusov = models.CharField(max_length=150)
    transmission = models.CharField(max_length=150)
    vinCode = models.CharField(max_length=8, unique=True, blank=True, null=True)

    def __str__(self):
        return self.userName

    @staticmethod
    def generate_vin_code():
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def save(self, *args, **kwargs):
        if not self.vinCode:
            self.vinCode = self.generate_vin_code()
        super().save(*args, **kwargs)