from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('history', views.history),
    path('process', views.process),
    path('support', views.support)
]
