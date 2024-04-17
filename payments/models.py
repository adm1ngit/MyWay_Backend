from django.db import models

# --------- Book evakuator Start --------------#
class Evakuator(models.Model):
    carModel = models.CharField(max_length=50)
    eventName = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    eventDate = models.DateField()

# --------- Book evakuator END --------------#

# --------- Book mechanic Start --------------#
class Mechanic(models.Model):
    eventName = models.CharField(max_length=250)
    carModel = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    eventDate = models.DateField()

# --------- Book mechanic END --------------#