from rest_framework import serializers
from .models import *


#---------- Manzillar START------------------------#



#---------- Manzillar END------------------------#

#-----------            ---------------------------#
class GasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gas
        fields = '__all__'
#-----------            ---------------------------#

#-----------            ---------------------------#
class CarOilSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarOil
        fields = '__all__'

#-----------            ---------------------------#

#---------------- Ishonchnoma START ----------------------#
class AffidavitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affidavit
        fields = '__all__'

#---------------- Ishonchnoma END ------------------------#

class TexServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TexServiceMessage
        fields = '__all__'

class RestoreLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestoreLicense
        fields = '__all__'

class AutoTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoTestResult
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'