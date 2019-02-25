from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='blog-home'),
    path('', views.welcome, name='blog-welcome'),
    path('about/', views.about, name='blog-about'),
]
