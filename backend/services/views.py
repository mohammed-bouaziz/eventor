from rest_framework.viewsets import ModelViewSet
from .models import Service
from .serializers import ServiceSerializer

class ServiceViewset(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)
    
    # def perform_update(self, serializer):
    #     serializer.save(created_by=self.request.user)