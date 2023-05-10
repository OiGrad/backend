from django.urls import path, include
from rest_framework import routers

from .views import CommentViewSet

app_name = 'comments'
router = routers.DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
]
