from django.urls import path
from . import views

urlpatterns = [
    path('cum/', views.sayCum),
    path('', views.getRoutes, name = "routes")
]