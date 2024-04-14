from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from .serializers import *
from .emails import *
from rest_framework.response import Response

class JarimaListCreate(generics.ListCreateAPIView):
    queryset = Jarima.objects.all()
    serializer_class = JarimaSerializer

# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            serializers = UserSerializer(data = data)
            if serializers.is_valid():
                serializers.save()
                send_otp_via_email(serializers.data['email'])
                return Response({
                    'status': 200,
                    'message': 'Registration successfully Check Email',
                    'data': serializers.data,
                })

            return Response({
                'status': 400,
                'message': "Something Went Wrong",
                'data': serializers.errors
            })
        except Exception as e:
            print(e)


class VerifyOtp(APIView):
    def post(self, request):
        try:
            data = request.data
            serializers = VerifyAccountSerializer(data=data)
        except Exception as e:
            print(e)
