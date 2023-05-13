from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        parent_type = self.request.query_params.get('parent_type', None)
        parent_id = self.request.query_params.get('parent_id', None)
        queryset = Comment.objects.all()
        if parent_type and parent_id:
            queryset = queryset.filter(parent_type=parent_type, parent_id=parent_id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
