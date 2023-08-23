from django.db import models
import datetime
from authentication.models import CustomUser

class Restaurant(models.Model):
    name = models.CharField(blank=True, max_length=256)

    id = models.AutoField(primary_key=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=datetime.datetime.now(), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now(), blank=True, null=True)

    users = models.ManyToManyField(CustomUser, related_name='restaurants')

    def __str__(self):

        return f"{self.id}-{self.name}"

    def __repr__(self):

        return f"Menu(id={self.id})"

    class Meta:
        app_label = 'restaurant'
