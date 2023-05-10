from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Post, Attachment
from .serializers import (
    PostSerializer,
    AttachmentSerializer,
)


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        post_type = request.data.get('type')
        content = request.data.get('content')
        index = request.data.get('index')

        # create post
        if post_type == 'image':
            img = request.data.get('img', None)
            post = Post.objects.create(user=request.user, img=img, body=content, index=index)

        elif post_type == 'place':
            place = request.data.get('place', None)
            post = Post.objects.create(user=request.user, place_id=place, body=content, index=index)

        else:
            post = Post.objects.create(user=request.user, body=content, index=index)

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
