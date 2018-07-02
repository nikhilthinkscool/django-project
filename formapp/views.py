# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from .forms import Userform
from .models import Signup

# Create your views here.

def index(request):
    return render (request, "formapp/index.html")


def login(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        try:
                user=Signup.objects.get(username=uname)
        except ObjectDoesNotExist:
                return render(request, 'form/login.html')        
