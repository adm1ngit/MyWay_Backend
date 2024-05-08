from django.urls import path
from .views import RegisterUserView, VerifyUserView, SendVerificationCodeView, VerifyVerificationCodeView, \
    PasswordResetRequestView, LoginView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('confirm-code/', VerifyUserView.as_view(), name='confirm-code'),
    path('send-verification-email/', SendVerificationCodeView.as_view(), name='send-verification-email'),
    path('verify-email/', VerifyVerificationCodeView.as_view(), name='verify-email'),
    path("login/", LoginView.as_view(), name="login"),
]
