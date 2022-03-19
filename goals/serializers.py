from rest_framework import serializers
from .models import Goal
from django.contrib.auth.models import User

class GoalSerializer(serializers.Serializer):
    class Meta:
        model = Goal
        fields = '__all__'

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'