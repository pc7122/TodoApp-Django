import math
import random

from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User


def generateOTP():
    digits = "0123456789"
    OTP = ""

    for i in range(6):
        OTP += digits[math.floor(random.random() * 10)]

    return OTP


def send_otp(email):
    OTP = generateOTP()
    subject = 'Verification Code'
    message = f'your verification code is {OTP}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]

    try:
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    except Exception:
        return False, None
    return True, OTP


def send_forget_password_mail(email, token):
    subject = 'Your forget password link'
    message = f'to reset your password, click on the link<br> http://127.0.0.1:8000/change-password/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email, ]

    try:
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)
    except Exception:
        return False
    return True


def validate(data, OTP):
    username = data['username']
    email = data['email']
    otp = data['otp']
    password = data['password']
    confirm_password = data['cpassword']

    user = None

    if not username:
        return False, 'Email should not be empty'

    if email:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass

        if user is not None:
            return False, 'Email already exist'
    else:
        return False, 'Email should not be empty'

    if otp != OTP:
        return False, 'invalid OTP'

    if len(password) < 8:
        return False, 'Password should be at least 8 letters'
    if password != confirm_password:
        return False, 'Password and Confirm should be same'

    return True, ''
