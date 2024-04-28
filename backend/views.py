from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

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
    queryset = AutoTestResult.objects.all()
    serializer_class = AutoTestSerializer
class DepartmentApi(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
