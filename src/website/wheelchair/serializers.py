from rest_framework import serializers

from wheelchair.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('station', 'door', 'time', 'user')
