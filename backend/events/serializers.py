from .models import Event, Session
from rest_framework.serializers import ModelSerializer


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'