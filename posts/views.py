from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from .serializers import PostSerializer, CommentSerializer, CommentReplaySerializer, AttachmentSerializer, LoveSerializer
from .models import Post, Comment, CommentReplay, Attachment


class PostAPIView(APIView):
    # Require authentication to create a post
    authentication_classes = []

    serializer_class = PostSerializer
    posts = Post.objects.all()

    def get(self, request, format=None):
        try:
            paginator = PageNumberPagination()
            paginated_posts = paginator.paginate_queryset(self.posts, request)
            serializer = PostSerializer(paginated_posts, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=404)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Set the user field to the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        try:
            item = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=404)
        serializer = PostSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Post.objects.get(pk=id)
        except Post.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PostDetail(APIView):
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    serializer_class = CommentSerializer

    def get(self, request, post_id):
        comments = Comment.objects.filter(post=post_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        request.data['post'] = post_id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):
    serializer_class = CommentSerializer

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk):
        comment = self.get_object(pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentReplayList(APIView):
    serializer_class = CommentReplaySerializer

    def post(self, request):
        serializer = CommentReplaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentReplayDetail(APIView):
    serializer_class = CommentReplaySerializer

    def get_object(self, pk):
        try:
            return CommentReplay.objects.get(pk=pk)
        except CommentReplay.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        comment_replay = self.get_object(pk)
        serializer = CommentReplaySerializer(comment_replay)
        return Response(serializer.data)

    def put(self, request, pk):
        comment_replay = self.get_object(pk)
        serializer = CommentReplaySerializer(comment_replay, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment_replay = self.get_object(pk)
        comment_replay.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AttachmentList(APIView):
    def post(self, request):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttachmentDetail(APIView):
    def get_object(self, pk):
        try:
            return Attachment.objects.get(pk=pk)
        except Attachment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        attachment = self.get_object(pk)
        serializer = AttachmentSerializer(attachment)
        return Response(serializer.data)

    def put(self, request, pk):
        attachment = self.get_object(pk)
        serializer = AttachmentSerializer(attachment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        attachment = self.get_object(pk)
        attachment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
