from rest_framework import serializers
from .models import UserProfile


# ------------------------------------------- UserProfile <-
class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
