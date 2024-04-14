from rest_framework import generics
from .models import *
from .serializers import *

class JarimaListCreate(generics.ListCreateAPIView):
    queryset = Jarima.objects.all()
    serializer_class = JarimaSerializer

