from django.contrib import admin
from .models import *

admin.site.register([JarimaBook, JarimaBookCategory])
admin.site.register([YHQQoidalarBook, YHQQoidlarCategory]),
admin.site.register(ServiceAddres),
admin.site.register(TexServiceOrder),
admin.site.register([Gas, CarOil]),
admin.site.register(Affidavit)
admin.site.register(TexServiceMessage)
admin.site.register(RestoreLicense)
admin.site.register(AutoTest)