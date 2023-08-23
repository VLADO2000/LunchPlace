from rest_framework import serializers
from menu.models import Menu
from rest_framework.exceptions import PermissionDenied

from restaurant.models import Restaurant
from restaurant.serializers import NestedRestaurantSerializer
class MenuSerializer(serializers.ModelSerializer):
    rest_repr = serializers.SerializerMethodField()
    rest_id = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = Menu
        fields = ['id', 'name', 'food_items', 'vote_count', 'rest_repr', 'rest_id','created_at', 'updated_at']
        read_only_fields = ('vote_count', 'rest_id_repr')

    def get_rest_repr(self, obj):
        return NestedRestaurantSerializer(obj.rest_id).data
    def validate(self, data):
        user = self.context['request'].user

        if user.role != 1:  # Check if the user's role is not 'restauranter'
            raise PermissionDenied("You don't have permission to create/update/delete menu items.")

        # Check if the user is associated with the restaurant of the menu
        restaurant_id = self.initial_data.get('rest_id')
        if restaurant_id:
            restaurant = self.instance.rest_id if self.instance else None
            if restaurant and user not in restaurant.users.all():
                raise PermissionDenied("You don't have permission to create/update menus for this restaurant.")

        return data

class NestedMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['name']