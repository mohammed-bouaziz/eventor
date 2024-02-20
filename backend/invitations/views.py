from .serializers import EventInvitationSerializer, SessionInvitationSerializer
from .models import EventInvitation, SessionInvitation
from rest_framework.viewsets import ModelViewSet

class EventInvitationViewset(ModelViewSet):
    queryset = EventInvitation.objects.all()
    serializer_class = EventInvitationSerializer

class SessionInvitationViewSet(ModelViewSet):
    queryset = SessionInvitation
    serializer_class = SessionInvitationSerializer