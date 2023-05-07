from rest_framework import generics, status, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import (
    PostSerializer,
    CommentSerializer,
    CommentReplaySerializer,
    AttachmentSerializer,
    LoveSerializer,
)
from .models import Post, Comment, CommentReplay, Attachment


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


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(post=post_id)

    def post(self, request, post_id, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user, post_id=post_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, post_id, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CommentReplayList(generics.CreateAPIView):
    queryset = CommentReplay.objects.all()
    serializer_class = CommentReplaySerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CommentReplayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentReplay.objects.all()
    serializer_class = CommentReplaySerializer

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
