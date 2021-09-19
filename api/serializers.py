from rest_framework import serializers
from links.models import Tag, Link


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class LinkSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Link
        fields = ('id', 'title', 'url', 'faviconUrl', 'tags')
