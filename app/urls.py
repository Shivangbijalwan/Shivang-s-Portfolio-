from django.urls import path
from app import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.handleSignup, name='signup'),
    path('login/', views.handleLogin, name='login'),
    path('logout/', views.handleLogout, name='logout'),
    path('contact/', views.contact, name='contact'),
]
