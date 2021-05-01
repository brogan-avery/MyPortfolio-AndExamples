from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pieChart', views.pieChart, name='pieChart'),
    path('lineChart', views.lineChart, name='lineChart'),
]
