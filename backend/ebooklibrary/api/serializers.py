from rest_framework import serializers
from . import models


class MemberSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Member
        fields = [
            'username', 
            'email', 
            'phone_number', 
            'password'
            ]

class MemberLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)