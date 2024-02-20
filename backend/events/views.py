from rest_framework import viewsets
from .models import Event, Session
from .serializers import EventSerializer, SessionSerializer

class EventViewset(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class =  EventSerializer

    # def perform_create(self, serializer):
    #     print(self.request.data)
    #     serializer.save(created_by=self.request.user)
    
    # def perform_update(self, serializer):
    #     serializer.save(created_by=self.request.user)

class SessionViewset(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)
    
    # def perform_update(self, serializer):
    #     serializer.save(created_by=self.request.user)



