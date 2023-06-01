from rest_framework import serializers
from about.models import About

class AboutFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"