from django.db import models
from django.contrib.auth.models import User


class PhoneOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=17, unique=True)
    otp = models.CharField(max_length=7, blank=True, null=True)
    validated = models.BooleanField(default=False, help_text='If it is true, that means user have validate OTP')
    object = models.manager

    def __str__(self):
        return self.phone + ' is sent ' + self.otp