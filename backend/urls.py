from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('api/jarima/', views.JarimaListCreate.as_view()),
    path('register/', RegisterAPI.as_view()),

]

