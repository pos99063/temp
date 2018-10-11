from django.shortcuts import render
from django.http import JsonResponse

class validation:
    def __init__(self):
        return

def login(request):
    print(request)
    return JsonResponse({"body":"HI"})