from django.urls import path
from . import views


urlpatterns = [
    path('rejestracja/', views.register, name='register'),
    path('', views.home, name='home'),
    path('zgloszenia/', views.ticket_list, name='ticket_list'),
    path('zgloszenia/nowe/', views.ticket_create, name='ticket_create'),
    path('zgloszenia/<int:pk>/', views.ticket_detail, name='ticket_detail'),
]