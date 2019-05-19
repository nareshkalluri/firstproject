from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def welcome(request):
    s="""<h1 align='center'>Welcome to my-site</h1>"""
    return HttpResponse(s)

import datetime
def timeinfo(reuest):
    date=datetime.datetime.now()
    s="the current date and time is: "+str(date)
    return HttpResponse(s)


