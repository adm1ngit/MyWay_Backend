from django.urls import path
from .views import *

urlpatterns = [
    path('api/jarimaBooks/', JarimaBooksAPIView.as_view()),
    path('api/Qoidalar/', YHQQoidlarBookAPIView.as_view()),
    path('api/Gas/', GasListCreateAPIView.as_view()),
    path('api/CarOil/', CarOilAPIView.as_view()),
    path('api/texmessage/', TexServiceMessageApi.as_view()),
    path('api/AutoTest/', AutoTestApi.as_view()),
    # path('api/manzillar/',),
]

