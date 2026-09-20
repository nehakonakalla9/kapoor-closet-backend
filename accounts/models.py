from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    mobile_number =  models.CharField(max_length=15)
    is_verified = models.BooleanField(default=False)


class OTPVerification(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    otp_code = models.CharField(max_length=4)
    expires_at = models.DateTimeField()