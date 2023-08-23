
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from .models import Restaurant
from .permissions import IsRestauranter, IsViewer
from .serializers import RestaurantSerializer



class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.action in ['retrieve', 'create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsRestauranter()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        # Associate the current user (manager) with the restaurant being created
        serializer.save(users=[self.request.user])

