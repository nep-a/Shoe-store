from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='list'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]
