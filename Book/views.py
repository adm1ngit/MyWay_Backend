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