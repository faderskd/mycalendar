from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    color = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('title', 'start', 'end', 'color', 'slug', 'url')

    def get_color(self, instance):
        return instance.category.color

    def get_url(self, instance):
        return instance.get_absolute_url()
