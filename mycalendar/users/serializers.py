from rest_framework import serializers
from django.templatetags.static import static
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'image_url',)

    def get_image_url(self, instance):
        if instance.photo:
            return instance.photo.url
        return static('images/default_profile_photo.png')