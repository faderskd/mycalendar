from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'title', 'start', 'end', 'color')

    def get_color(self, instance):
        return instance.category.color
