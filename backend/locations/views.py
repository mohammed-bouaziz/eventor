from .serializers import LocationSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Locations

class LocationViewset(ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationSerializer

    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

    # def perform_update(self, serializer):
    #     serializer.save(created_by=self.request.user)