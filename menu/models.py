import datetime

from django.db import models
from restaurant.models import Restaurant
class Menu(models.Model):

    name = models.CharField(blank=True, max_length=128)

    vote_count = models.IntegerField(default=0)
    id = models.AutoField(primary_key=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=datetime.datetime.now(), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=datetime.datetime.now(), blank=True, null=True)

    rest_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None)

    food_items = models.TextField()

    class Meta:
        ordering = ('id',)

    def __str__(self):

        return f"{self.id}-{self.name}"

    def __repr__(self):

        return f"Menu(id={self.id})"










