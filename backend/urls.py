from django.urls import path
from .views import *

urlpatterns = [
    path('api/jarima/', JarimaListApi.as_view()),
    path('api/qoidalar/',YHQQoidaListApi.as_view()),

]

