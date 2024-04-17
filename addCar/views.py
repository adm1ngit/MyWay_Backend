from rest_framework import generics
from rest_framework.response import Response
from .models import addCar
from .serializers import addCarSerializer

class addCarListCreate(generics.ListCreateAPIView):
    queryset = addCar.objects.all()
    serializer_class = addCarSerializer

    def post(self, request, *args, **kwargs):
        serializer = addCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

