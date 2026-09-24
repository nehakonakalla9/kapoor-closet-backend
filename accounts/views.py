from django.shortcuts import render
import random
from datetime import timedelta
import resend
from .models import User, OTPVerification
from rest_framework.views import APIView, Response
from django.conf import settings
from django.utils import timezone
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class SendOTPView(APIView):
    def post(self, request):
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        email= request.data['email']
        mobile_number = request.data['mobile_number']
        otp_code = random.randint(1000, 9999)
        expires_at = timezone.now() + timedelta(minutes=5)
        OTPVerification.objects.create(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            mobile_number = mobile_number,
            otp_code=otp_code, 
            expires_at=expires_at
            )
        resend.api_key = settings.RESEND_API_KEY
        resend.Emails.send({
            "from": "onboarding@resend.dev",
            "to": [email],
            "subject": "Your OTP code",
            "text": f"Your OTP is {otp_code}",
        })
        return Response({"message" : "OTP sent successfully"})


class VerifyOTPview(APIView):
    def post(self, request):
        email= request.data['email']
        otp_code = request.data['otp_code']
        record = OTPVerification.objects.filter(email=email).order_by('-id').first()
        if record is None:
            return Response({"message": "No pending verification for this email"})
        if record.otp_code != otp_code:
            return Response({"message" : "Incorrect OTP"})
        if timezone.now() > record.expires_at:
            return Response({"message" : "OTP Expired"})
        existing_user = User.objects.filter(email = record.email).first()
        if existing_user:
            user = existing_user
        else:
            user = User.objects.create(
                first_name = record.first_name,
                last_name = record.last_name,
                email = record.email,
                mobile_number = record.mobile_number,
                is_verified = True,
                username=record.email
            )
        refresh = RefreshToken.for_user(user)
        record.delete()
        return Response({
            "message" : "Verified Successfully",
            "access" : str(refresh.access_token),
            "refresh" : str(refresh)
            })