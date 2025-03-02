from rest_framework import serializers
from django.contrib.auth.models import User

#from .models import UserProfile


"""
Converts JSON input into a Django User model.
Hashes the password before saving (for security).
Returns JSON response after creating a user.

"""
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """Create a new user and return it"""
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),  # Email is optional
            password=validated_data['password']
        )
        return user
