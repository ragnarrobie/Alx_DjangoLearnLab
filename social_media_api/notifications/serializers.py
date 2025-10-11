# notifications/serializers.py
from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    target = serializers.CharField(source='target', read_only=True)  # display target as string

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target', 'timestamp', 'unread']
