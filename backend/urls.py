from django.urls import path
<<<<<<< Updated upstream
from . import views

urlpatterns = [
    path('api/jarima/', views.JarimaListCreate.as_view()),
=======
from .views import *

urlpatterns = [
    path('register/', RegisterAPI.as_view()),
>>>>>>> Stashed changes
]