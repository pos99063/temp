from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
## EMPTY VIEW

def index(request):
    return HttpRequest("hello world")