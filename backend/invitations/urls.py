from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventInvitationViewset, SessionInvitationViewSet

router = DefaultRouter()

router.register(r'event_invitation_crud', EventInvitationViewset, basename="event_invitation_crud")
router.register(r'session_invitation_crud', SessionInvitationViewSet, basename="session_invitation_crud")

urlpatterns = [
    path('', include(router.urls))
]
