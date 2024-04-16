from django.urls import path
from .views import *

urlpatterns = [
    path('api/jarima/', JarimaListApi.as_view()),
    path('api/belgilar/', YHQQoidaListApi.as_view()),
    path('api/manzillar/', AddressesListApi.as_view()),
]

