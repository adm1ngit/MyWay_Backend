from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('backend/', include("backend.urls")),
    path('book/', include("payments.urls")),
    path('addCar/', include("addCar.urls")),
    path('user/', include("user.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
