from django.urls import path
from . import views


urlpatterns = [
    path('rejestracja/', views.register, name='register'),
]