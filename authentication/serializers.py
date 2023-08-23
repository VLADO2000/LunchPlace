from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'password', 'email', 'role', 'is_active')

    def create(self, validated_data):


        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)