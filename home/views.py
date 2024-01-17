from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    template_index = ('index.html')
    return render(request, template_index)
