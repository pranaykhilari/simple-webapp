# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from allauth.account.views import SignupView, LoginView, ConfirmEmailView, EmailView, LogoutView
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
import json
from website.forms import *
from django.shortcuts import render, redirect

class Login(LoginView):
    form_class = UserLoginForm
    template_name = "login.html"

class Signup(SignupView):
    template_name = "signup.html"
    form_class = UserSignupForm

class ConfirmEmail(ConfirmEmailView):
    template_name = "email-confirmation.html"

class Email(EmailView):
    template_name = ""

def logout_user(request):
    logout(request)
    return redirect('/')

def profile(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
         return HttpResponse("Thanks")
    else:
        form = UserProfile(initial = {'name':request.user.username})

        return render(request, 'profile.html', {"form":form})

def check_user_contact(request):
    if request.method == 'GET':
        contact = request.GET.get('contact_number')
        if contact == "123":
            return HttpResponse(json.dumps("True"), content_type="application/json")
        else:
            return HttpResponse(json.dumps("False"), content_type="application/json")

def test_user(request):
    return HttpResponseRedirect("http://google.com/")