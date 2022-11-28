from rest_framework import serializers
from .models import UploadImages


class UploadImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadImages
        fields = ['image']