from django.urls import path
from app import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup', views.handleSignUp, name="handleSignUp"),
]
