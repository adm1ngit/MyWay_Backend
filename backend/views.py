from rest_framework import generics
from .serializers import *
from .models import *

class JarimaListCreate(generics.ListCreateAPIView):
    queryset = Jarima.objects.all()
    serializer_class = JarimaSerializer





