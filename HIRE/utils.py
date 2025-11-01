# HIRE/utils/email_otp

from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
import random
from HIRE.models import TBL_EMAIL_VERIFICATION

def send_otp_email(user, purpose):
    # Generate OTP
    otp = str(random.randint(100000, 999999))

    # ✅ FIXED: use lowercase field names
    TBL_EMAIL_VERIFICATION.objects.update_or_create(
        user=user,
        purpose=purpose,
        defaults={
            'otp': otp,
            'is_verified': False,
            'expires_at': timezone.now() + timedelta(minutes=10),
        }
    )

    # FIXED: correct user fields
    subject = "HireVerse Email Verification" if purpose == 'verify' else "HireVerse Password Reset OTP"
    message = (
        f"Dear {user.USER_NAME},\n\n"
        f"Your OTP to {'verify your HireVerse account' if purpose == 'verify' else 'reset your password'} is: {otp}\n\n"
        f"This code is valid for 10 minutes.\n\n"
        f"- HireVerse Team"
    )

    # Send email to correct user email field
    send_mail(
        subject,
        message,
        "hireversesystem@gmail.com",
        [user.EMAIL],  # Your model uses EMAIL
        fail_silently=False,
    )
