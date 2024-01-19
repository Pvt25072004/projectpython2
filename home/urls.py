from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('product', views.product),
    path('faq', views.faq),
    path('blog', views.blog),
    path('about', views.about),
    path('login', views.login),
    path('signup', views.signup),
]