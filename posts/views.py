from rest_framework import generics, status, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .serializers import PostSerializer, CommentSerializer, CommentReplaySerializer, AttachmentSerializer, \
    LoveSerializer
from .models import Post, Comment, CommentReplay, Attachment


class PostAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


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


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentReplayList(generics.CreateAPIView):
    queryset = CommentReplay.objects.all()
    serializer_class = CommentReplaySerializer


class CommentReplayDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentReplay.objects.all()
    serializer_class = CommentReplaySerializer


class AttachmentList(generics.CreateAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer


class AttachmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
