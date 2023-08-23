from rest_framework import serializers
from restaurant.models import Restaurant
from rest_framework.exceptions import PermissionDenied
class RestaurantSerializer(serializers.ModelSerializer):
    users_emails = serializers.SerializerMethodField()
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'created_at', 'updated_at', 'users_emails']
        read_only_fields = ('id','users_emails')

    def validate(self, data):
        user = self.context['request'].user

        if user.role != 1:  # Check if the user's role is not 'restauranter'
            raise PermissionDenied("You don't have permission to create a restaurant.")

        return data

    def get_users_emails(self, obj):
        # Extract and return a list of user emails from the related users instances
        return [user.email for user in obj.users.all()]


class NestedRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name']