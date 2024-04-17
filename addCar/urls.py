from django.urls import path
from .views import *

urlpatterns = [
    path('', addCarListCreate.as_view())
]