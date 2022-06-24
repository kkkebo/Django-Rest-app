from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    poster = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster', 'created']
