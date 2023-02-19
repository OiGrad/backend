from rest_framework import serializers
from posts.models import Post, Love, Comment, Attachment, CommentReplay


class LoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'


class CommentReplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReplay
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    commentreplay_set = CommentReplaySerializer(many=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
