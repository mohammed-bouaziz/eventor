from rest_framework.serializers import ModelSerializer
from .models import EventInvitation, SessionInvitation

class EventInvitationSerializer(ModelSerializer):
    class Meta:
        model = EventInvitation
        fields = "__all__"
    
class SessionInvitationSerializer(ModelSerializer):
    class Meta:
        model = SessionInvitation
        fields = "__all__"