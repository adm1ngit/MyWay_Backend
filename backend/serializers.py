from rest_framework import serializers
from .models import *

#------Jarimalar YHQ --------------#
class JarimaToifasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarimaToifasi
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarimaBandi
        fields = ['title', 'description', 'price_main', 'price_sale30', 'price_sale50']

class JarimaSerializer(serializers.ModelSerializer):
    category = JarimaToifasiSerializer()
    Band = BandSerializer(read_only=True)

    class Meta:
        model = Jarima
        fields = '__all__'
#------Jarimalar YHQ END --------------#

# -------- YHQ Qoidalar START-----------------#
class YHQQoidaSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = YHQQoida
        fields = ['id', 'text', 'img', 'category']

# -------- YHQ Qoidalar END -----------------#

#---------- Manzillar START------------------------#

class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = addresses
        fields = ['id', 'address', 'location']

#---------- Manzillar END------------------------#
