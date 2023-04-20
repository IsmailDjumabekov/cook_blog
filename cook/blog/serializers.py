from rest_framework import serializers
from .models import Post, Category, Tag, models

class PostSerializer(serializers.Serializer):
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    text = serializers.TextField()
    category_id = serializers.IntegerField()
    slug = serializers.SlugField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author_id = validated_data.get('author_id', instance.author_id)
        instance.title = validated_data.get('title', instance.title)
        instance.image = validated_data.get('image', instance.image)
        instance.text = validated_data.get('text', instance.text)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance