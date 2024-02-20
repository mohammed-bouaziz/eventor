from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ServiceViewset

router = DefaultRouter()

router.register(r'crud', ServiceViewset, basename='crud')

urlpatterns = [
    path('', include(router.urls))
]
