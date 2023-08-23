from django.db import models, DataError
from authentication.models import CustomUser
from menu.models import Menu

from datetime import timedelta
from django.utils import timezone


class Vote(models.Model):



    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(default=None, null=True, blank=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE, default=None)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        return str(self.id)
