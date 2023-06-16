from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from places.models import Place
from .models import Post, Attachment, PostContent
from .serializers import (
    PostSerializer,
    AttachmentSerializer,
)


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        contents = request.data.get('contents')
        post = Post.objects.create(user=request.user)

        for content in contents:
            # create post
            content_type = content.get('type', None)
            if content_type == 'image':
                img = content.get('img', None)
                post_content = PostContent.objects.create(img=img, type=content_type, post=post)

            elif content_type == 'place':
                place_id = content.get('place_id', None)
                place = Place.objects.get(id=place_id)
                post_content = PostContent.objects.create(place=place, type=content_type, post=post)
            else:
                text = content.get('text', None)
                post_content = PostContent.objects.create(type=content_type, post=post, text=text)

        return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AttachmentList(generics.CreateAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
