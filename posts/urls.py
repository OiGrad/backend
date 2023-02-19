from django.urls import path
from .views import PostAPIView, PostDetail, CommentList, CommentDetail, CommentReplayList, CommentReplayDetail, AttachmentList, AttachmentDetail

urlpatterns = [
    path('post/', PostAPIView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('post/<int:post_id>/comments/', CommentList.as_view(), name='comment_list'),

    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment_detail'),
    path('comment-replays/', CommentReplayList.as_view(), name='comment_replay_list'),
    path('comment-replays/<int:pk>/', CommentReplayDetail.as_view(), name='comment_replay_detail'),

    path('attachments/', AttachmentList.as_view(), name='attachment_list'),
    path('attachments/<int:pk>/', AttachmentDetail.as_view(), name='attachment_detail'),
]
