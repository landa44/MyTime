from contextlib import redirect_stderr
from sys import stderr
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from accounts.models import Token
from django.urls import reverse
from django.contrib import auth

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )

    message_body = f'Use this link to log in \n\n{url}'

    send_mail(
        'Your login link for Superlists',
        message_body,
        'tdd_landa44@gmail.com',
        [email],
    )

    messages.success(
        request, 
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    user = auth.authenticate(uid=request.GET.get('token'))
    if user:
        auth.login(request, user)
        
    return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')