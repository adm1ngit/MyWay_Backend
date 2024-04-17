from django.urls import path
from .views import *

urlpatterns = [
    path('evakuator/', EvakuatorListCreate.as_view()),
    path('avtomexanik/', MechanicListCreate.as_view()),
]