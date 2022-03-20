from django.forms import CharField
from rest_framework import serializers



class UploadFileSerializer(serializers.Serializer):
    file=serializers.FileField()
    