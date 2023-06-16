from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Post, Attachment, Love, PostContent


class LoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostContent
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    contents = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'contents', 'likes', 'created_at', 'updated_at']

    def get_likes(self, obj):
        return obj.likes.count()

    def get_contents(self, obj):
        return ContentSerializer(PostContent.objects.filter(post=obj), many=True).data
