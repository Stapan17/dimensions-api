from rest_framework import serializers
from .models import dim


class dimSerializer(serializers.ModelSerializer):
    class Meta:
        model = dim
        fields = ['image_height', 'image_width']
