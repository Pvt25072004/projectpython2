from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>Welcome to My Project</h1>')
    response.write('<p>This is my app</p>')
    return response
