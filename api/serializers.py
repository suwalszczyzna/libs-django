from rest_framework import serializers
from links.models import Tag, Link


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class LinkSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Link
        fields = ['id', 'title', 'url', 'faviconUrl', 'tags', 'created']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags') or []
        link = Link.objects.create(**validated_data)
        for item in tags_data:
            name = item.get('name')
            if name:
                tag, _ = Tag.objects.get_or_create(name=name)
                link.tags.add(tag)

        return link
