from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>Welcome to my github</h1>')
    return response
