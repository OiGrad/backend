from django.urls import path

from posts import views
from posts.views import PostAPIView

urlpatterns = [

    path('<int:id>/', PostAPIView.as_view(), name='post'),
    path('', views.PostAPIListView.as_view(), name='post_list_create'),
   
   # path('love/<int:id>/', views.LoveAPIView.as_view()),
   # path('love/', views.LoveAPIListView.as_view()),

    #path('comment/<int:id>/', views.CommentAPIView.as_view()),
    #path('comment/', views.CommentAPIListView.as_view()),

    #path('attachment/<int:id>/', views.AttachmentAPIView.as_view()),
    #path('attachment/', views.AttachmentAPIListView.as_view()),

]
