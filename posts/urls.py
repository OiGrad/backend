from django.urls import path
from .views import PostAPIView, PostDetail, CommentDetail, CommentList, CommentReplayList, AttachmentList

urlpatterns = [
    path('', PostAPIView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),

    path('<int:post_id>/comments/', CommentList.as_view(), name='comment_list'),
    path('comments/<int:comment_id>/replies/', CommentReplayList.as_view(), name='comment_replies'),

    path('post/<int:post_id>/attachments/', AttachmentList.as_view(), name='attachment_list'),
]
