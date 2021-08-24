from django.urls import path, include
from .import views


urlpatterns = [
    path('', views.index),
    path('index_sch/', views.index_sch),
]