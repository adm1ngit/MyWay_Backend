from rest_framework import serializers
from .models import *
from twilio.rest import Client
import os

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User  
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            email=validated_data.get('email'), 
            password=validated_data['password'],
        )
        user.is_verified = False
        user.save()
        return user

class ConfirmationCodeSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=20)
    code = serializers.CharField(max_length=6)

class TwilioVerificationService:
    def __init__(self):
        self.client = Client(os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"))

class UserVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVerification
        fields = ["email", "verification_code"]

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class LoginUserVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVerification
        fields = ("phone_verification_code", "email_verification_code")


