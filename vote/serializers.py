from datetime import datetime, timedelta

from rest_framework import serializers

from menu.serializers import MenuSerializer, NestedMenuSerializer
from vote.models import Vote
from menu.models import Menu

from rest_framework.exceptions import PermissionDenied

class VoteSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    menu_id = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
    menu = serializers.SerializerMethodField()



    class Meta:
        model = Vote
        fields = ['id','menu','menu_id', 'user', 'created_at']
        read_only_fields = ('id', 'user', 'menu_id')

    def get_menu(self, obj):
        return NestedMenuSerializer(obj.menu_id).data

    def validate(self, data):
        user = self.context['request'].user

        if user.role == 1:  # Check if the user's role is 'restauranter'
            raise PermissionDenied("Restauranter users are not allowed to create votes.")


        return data

    def create(self, validated_data):
        menu = validated_data['menu_id']
        user = validated_data['user']
        existing_votes = Vote.objects.filter(user=user, end_at__isnull=False)
        if existing_votes.exists():
            raise PermissionDenied("You can't create a new vote until your existing votes have ended.")


        # Increment the vote_count of the associated menu
        menu.vote_count += 1
        menu.save()

        end_date = datetime.now() + timedelta(hours=23)

        # Set the end date for the new vote
        validated_data['end_at'] = end_date

        # Create the vote object
        vote = Vote.objects.create(**validated_data)


        return vote

