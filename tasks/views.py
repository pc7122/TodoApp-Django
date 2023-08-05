from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Tasks
from .helper import send_forget_password_mail, send_otp, validate

import uuid

TOKEN = str(uuid.uuid4())
OTP = None


def login_view(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'tasks/login.html')


def forget_password(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST.get('username', None)

        if username is not None:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return render(request, 'tasks/forget_password.html')

            email_sent = send_forget_password_mail(user.email, TOKEN)
            if email_sent:
                messages.info(request, 'Reset password link is sent to your mail', extra_tags='forget_password')
            else:
                messages.error(request, 'Something went wrong, Please try again.', extra_tags='forget_password')

    return render(request, 'tasks/forget_password.html')


def change_password(request: HttpRequest, token):
    if request.method == 'POST':
        password = request.POST.get('password', None)
        cpassword = request.POST.get('cpassword', None)

        if password is not None and password == cpassword:
            try:
                user = User.objects.get(username=request.user)
                user.set_password(password)
                user.save()

                return redirect('/login/')

            except User.DoesNotExist:
                messages.error(request, 'User does not exist.', extra_tags='change_password')
        else:
            messages.error(request, 'Password and Confirm Password does not match.', extra_tags='change_password')

    if token == TOKEN:
        return render(request, 'tasks/change_password.html', {'token': token})
    else:
        messages.error(request, 'Invalid token.', extra_tags='forget_password')
        return redirect('forget_password')


def register(request: HttpRequest):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        otp = request.POST['otp']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        status, msg = validate(request.POST.dict(), OTP)
        if status:
            user = User.objects.create_user(username, email, password)
            user.email = email
            user.save()
            return redirect('/login/')
        else:
            messages.error(request, msg, extra_tags='register')

    return render(request, 'tasks/register.html')


@login_required(login_url='/login/')
def logout_view(request: HttpRequest):
    logout(request)
    return redirect('/login/')


@login_required(login_url='/login/')
def task_list(request: HttpRequest):
    tasks = Tasks.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'tasks/taskslist.html', context)


@login_required(login_url='/login/')
@require_http_methods(['POST'])
def add_task(request: HttpRequest):
    title = request.POST.get('title', '')
    if title:
        user = request.user
        task = Tasks(user=user, title=title)
        task.save()
    return redirect('/')


@login_required(login_url='/login/')
def update_task(request: HttpRequest, tid: int):
    task = Tasks.objects.get(id=tid)
    task.complete = not task.complete
    task.save()
    return redirect('/')


@login_required(login_url='/login/')
def delete_task(request: HttpRequest, tid: int):
    task = Tasks.objects.get(id=tid)
    task.delete()
    return redirect('/')


@require_http_methods(['POST'])
def get_otp(request: HttpRequest):
    global OTP
    email = request.POST['email']
    status, OTP = send_otp(email)
    return JsonResponse({'status': status})
