import logging
import os
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import random
from django.core.mail import send_mail
from twilio.rest import Client
from .models import UserVerification, User


logger = logging.getLogger(__name__)


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< USER REGISTRATION START <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

class RegisterUserView(APIView):
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        verification_service_sid = os.getenv("VERIFICATION_SERVICE_SID")
        verification = client.verify \
                             .services(verification_service_sid) \
                             .verifications \
                             .create(to=user.phone_number, channel='sms')

        if verification.status == 'pending':
            return Response({'message': 'Verification code sent to your phone number.'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'Failed to send verification code.'}, status=status.HTTP_400_BAD_REQUEST)




class VerifyUserView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        verification_code = request.data.get('verification_code')

        if not phone_number or not verification_code:
            return Response({'message': 'Telefon raqami yoki tasdiqlash kodini kiritish talab qilinadi'}, status=status.HTTP_400_BAD_REQUEST)

        verification_service_sid = os.getenv("VERIFICATION_SERVICE_SID")
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)

        try:
            verification_check = client.verify \
                                       .services(verification_service_sid) \
                                       .verification_checks \
                                       .create(to=phone_number, code=verification_code)
            if verification_check.status == 'approved':
                return Response({'message': "Tasdiqlash muvaffaqiyatli Amalga Oshirildi"}, status=status.HTTP_200_OK)
            else:
                return Response({'message': "Noto'g'ri tasdiqlash kod"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< USER REGISTRATION END <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< USER PASSWORD RESET START <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class SendVerificationCodeView(APIView):
    def post(self, request):
        serializer = UserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]


        verification_code = str(random.randint(100000, 999999))

        subject = "Verification Code"
        message = f"Your verification code is: {verification_code}"
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

        if send_mail:
            user_verification, created = UserVerification.objects.get_or_create(email=email)
            user_verification.verification_code = verification_code
            user_verification.save()

            return Response({"message": "Verification code sent successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Failed to send verification code."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class VerifyCodeView(APIView):
    def post(self, request):
        serializer = UserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        entered_code = serializer.validated_data["verification_code"]

        try:
            user_verification = UserVerification.objects.get(verification_code=entered_code)

            user = authenticate(identifier=user_verification.identifier)
            if user:
                return Response({"message": "Verification successful."}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        except UserVerification.DoesNotExist:
            return Response({"message": "Invalid verification code."}, status=status.HTTP_400_BAD_REQUEST)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< USER PASSWORD RESET END <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< USER LOGIN START <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
class LoginView(APIView):
    def post(self, request):
        serializer = LoginUserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = request.data.get("phone_number")
        email = request.data.get("email")


        try:
            user = User.objects.get(email=email)  
        except User.DoesNotExist:
            return Response({"message": "Foydalanuvchi Topilmadi"}, status=status.HTTP_404_NOT_FOUND)

   
        phone_verification_code = str(random.randint(100000, 999999))
        email_verification_code = str(random.randint(100000, 999999))

        
        user_verification, created = UserVerification.objects.get_or_create(user=user)
        user_verification.phone_number = phone_number 
        user_verification.phone_verification_code = phone_verification_code
        user_verification.email_verification_code = email_verification_code
        user_verification.save()

       
        account_sid = os.getenv("ACCOUNT_SID")
        auth_token = os.getenv("AUTH_TOKEN")
        client = Client(account_sid, auth_token)
        if phone_number:  
            client.messages.create(
                 to=phone_number,
                 from_=os.getenv("TWILIO_PHONE_NUMBER"),
                 body=f"Your phone verification code is: {phone_verification_code}"
            )

        if email:  
            subject = "Email Verification Code"
            message = f"Your email verification code is: {email_verification_code}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

        return Response({"message": "Verification codes sent."}, status=status.HTTP_200_OK)




# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< USER LOGIN END <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<