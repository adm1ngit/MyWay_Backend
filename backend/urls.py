from django.urls import path
from . import views

urlpatterns = [
    path('api/jarima/', views.JarimaListCreate.as_view()),
]