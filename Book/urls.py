from django.urls import path
from .views import *
urlpatterns = [
    path('api/belgilar', JarimaBooksAPIView.as_view()),
    path('api/jarimalar', YHQQoidlarBookAPIView.as_view())
]