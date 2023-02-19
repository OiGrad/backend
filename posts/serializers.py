from rest_framework import serializers
from .models import Post, Comment, CommentReplay, Attachment, Love


class LoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class CommentReplaySerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = CommentReplay
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()


class CommentSerializer(serializers.ModelSerializer):
    commentreplay_set = CommentReplaySerializer(many=True)
    replies = CommentReplaySerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()
