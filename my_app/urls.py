from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
]
