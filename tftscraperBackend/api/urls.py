from django.contrib import admin
from django.urls import path, include
from api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'carryAndComps', CarryAndCompsViewSet)

urlpatterns= [
  # path('', getData, name = "data"),
  # path('wel/', ReactView.as_view(), name="compData"),
  path('', include(router.urls)),
  path('api-auth/', include('rest_framework.urls'))
]