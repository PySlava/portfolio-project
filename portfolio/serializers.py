from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'author', 'tags')
