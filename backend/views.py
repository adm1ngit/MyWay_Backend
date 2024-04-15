from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class JarimaListApi(generics.ListCreateAPIView):
    queryset = Jarima.objects.all()
    serializer_class = JarimaSerializer


class YHQQoidaListApi(APIView):
    def get(self, request):
        yhqqoidalar = YHQQoida.objects.all()
        serializer = YHQQoidaSerializer(yhqqoidalar, many=True)
        return Response(serializer.data)



