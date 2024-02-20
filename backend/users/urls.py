from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewset, ProfileVieset

router =  DefaultRouter()
router.register(r'register', CustomUserViewset)
router.register(r'profile', ProfileVieset, basename='profile')

urlpatterns = [
    path('', include(router.urls))
]
