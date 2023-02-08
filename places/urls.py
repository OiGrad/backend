from django.conf.urls import include
from django.urls import path

from places import views

urlpatterns = [

    path('city/<int:id>/', views.CityAPIView.as_view()),
    path('city/', views.CityAPIListView.as_view()),

    path('placecategory<int:id>/', views.PlaceCategoryAPIView.as_view()),
    path('placecategory/', views.PlaceCategoryAPIListView.as_view()),

    path('place/<int:id>/', views.PlaceAPIView.as_view()),
    path('place/', views.PlaceAPIListView.as_view()),

    path('placegallery/<int:id>/', views.PlaceGalleryAPIView.as_view()),
    path('placegallery/', views.PlaceGalleryAPIListView.as_view()),

    path('placereview/<int:id>/', views.PlaceReviewAPIView.as_view()),
    path('^placereview/', views.PlaceReviewAPIListView.as_view()),

    path('user/favorite', views.UserActionsAPI.as_view()),
]
