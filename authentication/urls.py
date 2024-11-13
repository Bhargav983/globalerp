from django.urls import path
from . import views

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
]