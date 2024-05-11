from rest_framework import serializers
from .models import *

#------Jarimalar YHQ --------------#
class JarimaBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarimaBook
        fields = '__all__'

#------Jarimalar YHQ END --------------#

# -------- YHQ Qoidalar START -----------------#
class YHQQoidalarBookSerializer(serializers.ModelSerializer):
    categoryRu = serializers.CharField(source='categoryRu.categoryRu')
    categoryUz = serializers.CharField(source='categoryUz.categoryUz')
    class Meta:
        model = YHQQoidalarBook
        fields = '__all__'

# -------- YHQ Qoidalar END -----------------#