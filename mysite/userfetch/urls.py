from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('userfetch/', views.index, name='index'),
]