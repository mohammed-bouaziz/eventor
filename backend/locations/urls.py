from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LocationViewset

router = DefaultRouter()

router.register(r'crud', LocationViewset, basename="crud")

urlpatterns = [
    path('', include(router.urls))
]
