from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('confirm_code/', VerifyUserView.as_view(), name='confirm_code'),
    path('send_verification_email/', SendVerificationCodeView.as_view(), name='send_verification_email'),
    path('verify_email/', VerifyCodeView.as_view(), name='verify_email'),
    path("login/", LoginView.as_view(), name="login"),
]
