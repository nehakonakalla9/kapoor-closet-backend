from django.urls import path
from .views import SendOTPView, VerifyOTPview

urlpatterns =[ 
    path('register/', SendOTPView.as_view()),
    path('verify/', VerifyOTPview.as_view())
]