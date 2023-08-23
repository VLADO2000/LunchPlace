from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import Menu

from .serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from django.db.models import F
from django.utils import timezone
from django.db.models.functions import TruncDate


# Simulate tomorrow's date to see an empty list for tommorow
#tomorrow_date = timezone.now().date() + timedelta(days=1)
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.annotate(
        created_date=TruncDate('created_at')
    ).filter(
        created_date=timezone.now().date()
    )
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

    def check_object_permissions(self, request, obj):
        """
        Check if the requesting user has permission to perform the action on the object.
        """
        super().check_object_permissions(request, obj)

        user = request.user

        if self.action == 'destroy' and user.role != 1:
            raise PermissionDenied("You don't have permission to delete this menu item.")


class DayMenuViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        today = datetime.now().date()
        highest_vote_menus = Menu.objects.filter(created_at__date=today).order_by('-vote_count')

        if highest_vote_menus:
            highest_vote = highest_vote_menus.first().vote_count
            highest_vote_menus = highest_vote_menus.filter(vote_count=highest_vote)

            serializer = MenuSerializer(highest_vote_menus, many=True)
            return Response(serializer.data)
        else:
            return Response({"message": "No menu found for today."})