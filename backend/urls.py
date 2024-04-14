from django.urls import path
from .views import *

urlpatterns = [
    path('api/jarima/', JarimaListCreate.as_view()),
    path('register/', RegisterAPI.as_view()),
]