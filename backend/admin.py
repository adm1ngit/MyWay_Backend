from django.contrib import admin
from .models import *

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'phone_number']


admin.site.register(User, UserModelAdmin)
admin.site.register(UserConfirmation)
admin.site.register(JarimaToifasi),
admin.site.register(Jarima),
admin.site.register(Band),


