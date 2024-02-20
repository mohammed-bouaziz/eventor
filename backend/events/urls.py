from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewset, SessionViewset

router = DefaultRouter()

router.register(r'crud', EventViewset, basename="crud")
router.register(r'session_crud', SessionViewset, basename="session_crud")

urlpatterns = [
    path('', include(router.urls))
]




