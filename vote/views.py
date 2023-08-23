from rest_framework import viewsets, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from rest_framework.views import APIView

from authentication.models import CustomUser


from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Vote
from .serializers import VoteSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if user.role == 0:  # Visitor
                return Vote.objects.filter(user=user)

        raise PermissionDenied("You don't have permission to view votes as you belong to managers.")

    def perform_destroy(self, instance):




        # Decrement the vote_count of the associated menu
        menu = instance.menu_id
        menu.vote_count -= 1
        menu.save()



        # Delete the vote instance
        instance.delete()

