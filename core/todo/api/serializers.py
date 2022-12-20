from ..models import Todo
from rest_framework import serializers


class TodoSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    is_completed = serializers.BooleanField(default=False)
    class Meta:
        model = Todo
        exclude = ('created_at', 'updated_at')