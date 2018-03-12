from django.urls import path

from . import views

urlpatterns = [
    path('glowapp/', views.map, name='map'),
]
