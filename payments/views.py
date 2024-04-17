from rest_framework import generics
from rest_framework.response import Response
from .models import Evakuator, Mechanic
from .serializers import EvakuatorSerializer, MechanicSerializer

class EvakuatorListCreate(generics.ListCreateAPIView):
    queryset = Evakuator.objects.all()
    serializer_class = EvakuatorSerializer

    def post(self, request, *args, **kwargs):
        serializer = EvakuatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class MechanicListCreate(generics.ListCreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer

    def post(self, request, *args, **kwargs):
        serializer = MechanicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
