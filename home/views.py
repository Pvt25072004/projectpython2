from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    template_home = ('page/home.html')
    return render(request, template_home)
def product(request):
    template_product = ('page/product.html')
    return render(request, template_product)
def faq(request):
    template_faq = ('page/faq.html')
    return render(request, template_faq)
def blog(request):
    template_blog = ('page/blog.html')
    return render(request, template_blog)
def about(request):
    template_about = ('page/about.html')
    return render(request, template_about)
def login(request):
    template_login = ('page/login.html')
    return render(request, template_login)
def signup(request):
    template_signup = ('page/signup.html')
    return render(request, template_signup)
