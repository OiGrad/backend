from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Post, Attachment, Love


class LoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    attachments = AttachmentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes(self, obj):
        return obj.likes.count()
