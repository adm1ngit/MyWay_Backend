from rest_framework import serializers
from .models import *

#------Jarimalar YHQ --------------#
class JarimaBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarimaBook
        fields = '__all__'

#------Jarimalar YHQ END --------------#

# -------- YHQ Qoidalar START-----------------#
class YHQQoidalarBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = YHQQoidalarBook
        fields = '__all__'

# -------- YHQ Qoidalar END -----------------#

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
        model = AutoTest
        fields = '__all__'
