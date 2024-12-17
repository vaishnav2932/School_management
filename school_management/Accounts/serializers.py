from rest_framework import serializers
from .models import *

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, help_text="Enter your username address.")
    password = serializers.CharField(required = True, help_text="Enter your password.")