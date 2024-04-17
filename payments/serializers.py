from rest_framework import serializers
from .models import *

class EvakuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evakuator
        fields = '__all__'

class MechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mechanic
        fields = '__all__'