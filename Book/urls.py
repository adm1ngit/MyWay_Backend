from django.urls import path
from .views import *
urlpatterns = [
    path('api/belgilar', YHQQoidlarBookAPIView.as_view()),
    path('api/jarimalar', JarimaBooksAPIView.as_view())
]