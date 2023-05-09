from django.urls import path
from .views import *


app_name = "otp_verification"

urlpatterns = [
    path("otp-send/", OTPsend.as_view(), name="otp-send"),
    path("otp-verify/", OTPverify.as_view(), name="otp-verify"),
]
