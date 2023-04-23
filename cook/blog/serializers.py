from rest_framework import serializers
from .models import Post, Category, Tag, models


class PostSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    author_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    image = serializers.ImageField()
    text = serializers.TextField()
    category_id = serializers.IntegerField()
    slug = serializers.SlugField()

