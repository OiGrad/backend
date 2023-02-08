from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from posts.serializers import PostSerializer, LoveSerializer, CommentSerializer, AttachmentSerializer
from posts.models import Post, Love, Comment, Attachment


class PostAPIView(RetrieveUpdateDestroyAPIView):
    authentication_classes = []
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, id, format=None):
        try:
            item = Post.objects.get(pk=id)
            serializer = PostSerializer(item)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=404)

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


class PostAPIListView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    authentication_classes = []



    def get(self, request, format=None):
        posts = Post.objects.prefetch_related( 'comment_set__commentreplay_set',).all().order_by('-updated_at')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    #the meaning of life ?
    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoveAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

    def get(self, request, id, format=None):
        try:
            item = Love.objects.get(pk=id)
            serializer = LoveSerializer(item)
            return Response(serializer.data)
        except Love.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Love.objects.get(pk=id)
        except Love.DoesNotExist:
            return Response(status=404)
        serializer = LoveSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Love.objects.get(pk=id)
        except Love.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class LoveAPIListView(ListCreateAPIView):
    serializer_class = LoveSerializer
    queryset = Love.objects.all()

    def get(self, request, format=None):
        items = Love.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = LoveSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = LoveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CommentAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Comment.objects.get(pk=id)
            serializer = CommentSerializer(item)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            return Response(status=404)
        serializer = CommentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Comment.objects.get(pk=id)
        except Comment.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CommentAPIListView(APIView):

    def get(self, request, format=None):
        items = Comment.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CommentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class AttachmentAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Attachment.objects.get(pk=id)
            serializer = AttachmentSerializer(item)
            return Response(serializer.data)
        except Attachment.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Attachment.objects.get(pk=id)
        except Attachment.DoesNotExist:
            return Response(status=404)
        serializer = AttachmentSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Attachment.objects.get(pk=id)
        except Attachment.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class AttachmentAPIListView(APIView):

    def get(self, request, format=None):
        items = Attachment.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = AttachmentSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
