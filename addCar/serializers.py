from rest_framework import serializers
from .models import addCar
import random
import string

class addCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = addCar
        fields = '__all__'


