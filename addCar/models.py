from django.db import models
import random
import string

class Car(models.Model):
    vinCode = models.CharField(max_length=17, unique=True, blank=True, null=True)
    carNum = models.CharField(max_length=2)
    carFullNum = models.IntegerField()
    texSeries = models.CharField(max_length=10)
    texNum = models.CharField(max_length=10)
    dateStart = models.DateField()
    dateEnd = models.DateField()
    avtoMark = models.CharField(max_length=20)
    avtoName = models.CharField(max_length=20)
    avtoYear = models.IntegerField()
    avtoEngine = models.CharField(max_length=50)
    avtoColor = models.CharField(max_length=50)

    # avtoBuyDate = models.DateField()
    avtoCusov = models.CharField(max_length=150)
    transmission = models.CharField(max_length=150)

    def __str__(self):
        return self.userName

    # @staticmethod
    # def generate_vin_code():
    #     return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    #
    # def save(self, *args, **kwargs):
    #     if not self.vinCode:
    #         self.vinCode = self.generate_vin_code()
    #     super().save(*args, **kwargs)