from rest_framework import serializers
from posts.models import Post, Love, Comment, Attachment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created_at', 'updated_at')


class LoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
