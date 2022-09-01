
from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "name",
            "last_name",
            "city",
            "age",
            "designation",
            "exprience",
        ]