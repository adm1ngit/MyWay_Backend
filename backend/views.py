from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class JarimaBooksAPIView(APIView):
    def get(self, request):
        jarimaBook = JarimaBook.objects.all()
        serializer = JarimaBooksSerializer(jarimaBook, many=True,  context={'request': request})
        return Response(serializer.data)



class YHQQoidlarBookAPIView(APIView):
    def get(self, request):
        queryset = YHQQoidalarBook.objects.all()
        serializer = YHQQoidalarBookSerializer(queryset, many=True,  context={'request': request})
        return Response(serializer.data)


class GasListCreateAPIView(generics.ListCreateAPIView):
    queryset = Gas.objects.all()
    serializer_class = GasSerializer

class CarOilAPIView(generics.ListCreateAPIView):
    queryset = CarOil.objects.all()
    serializer_class = CarOilSerializer

class AffidavitApiView(generics.ListCreateAPIView):
    queryset = Affidavit.objects.all()
    serializer_class = AffidavitSerializer


class TexServiceMessageApi(generics.ListCreateAPIView):
    queryset = TexServiceMessage.objects.all()
    serializer_class = TexServiceSerializer

class RestoreLicenseApi(generics.ListCreateAPIView):
    queryset = RestoreLicense.objects.all()
    serializer_class = RestoreLicenseSerializer

class AutoTestApi(generics.ListCreateAPIView):
    queryset = AutoTest.objects.all()
    serializer_class = AutoTestSerializer
