from django.shortcuts import render
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    return render(request,"Hello.html");
# Create your views here.
