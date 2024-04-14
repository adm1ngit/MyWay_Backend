from rest_framework import serializers
<<<<<<< Updated upstream
from .models import *

#------Jarimalar YHQ ---------
class JarimaToifasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = JarimaToifasi
        fields = '__all__'

class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['title', 'description', 'price_main', 'price_sale30', 'price_sale50']

class JarimaSerializer(serializers.ModelSerializer):
    category = JarimaToifasiSerializer()
    Band = BandSerializer(read_only=True)

    class Meta:
        model = Jarima
        fields = '__all__'
#------Jarimalar YHQ END ---------
=======
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']


class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
>>>>>>> Stashed changes
