from rest_framework import serializers
from .models import *


class PhoneOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneOTP
        # fields = '__all__'
        fields = ['phone', 'otp']