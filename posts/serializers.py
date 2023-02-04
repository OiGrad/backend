from rest_framework.serializers import ModelSerializer
from posts.models import Post, Love, Comment, Attachment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'updated_at']


class LoveSerializer(ModelSerializer):
    class Meta:
        model = Love
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AttachmentSerializer(ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
