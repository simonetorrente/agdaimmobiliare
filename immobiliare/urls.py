from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agenti/', views.agenti, name='agenti'),
    path('immobili/', views.immobili, name='immobili'),
    path('immobili/<int:pk>', views.immobile, name='immobile'),
]

