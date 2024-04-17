from rest_framework import generics
from rest_framework.response import Response
from .serializers import addCarSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .models import Car
class addCarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = addCarSerializer

    def post(self, request, *args, **kwargs):
        serializer = addCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CarDetailsByVinCode(APIView):
    def get(self, request):
        vincode = request.query_params.get('vincode', None)
        if not vincode:
            return Response({'error': 'VinCode parametri kiritilmagan'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            car = Car.objects.get(vinCode=vincode)
        except Car.DoesNotExist:
            return Response({'error': 'Avtomobil topilmadi'}, status=status.HTTP_404_NOT_FOUND)

        car_details = {
            'username': car.userName,
            'email': car.email,
            'carNamber': car.carNamber,
            'avtoMark': car.avtoMark,
            'avtoName': car.avtoName,
            'avtoYear': car.avtoYear,
            'avtoEngine': car.avtoEngine,
            'avtoColor': car.avtoColor,
            'docNumber': car.docNumber,
            'docDate': car.docDate,
            'politicalNum': car.politicalNum,
            'dateStart': car.dateStart,
            'dateEnd': car.dateEnd,
            'avtoBuyDate': car.avtoBuyDate,
            'avtoPrice': car.avtoPrice,
            'avtoCusov': car.avtoCusov,
            'transmission': car.transmission,
        }
        return JsonResponse(car_details)