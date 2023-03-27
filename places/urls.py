from django.conf.urls import include
from django.urls import path, re_path

from places import views

urlpatterns = [

    path('city/<int:id>/', views.CityAPIView.as_view()),
    path('city/', views.CityAPIListView.as_view()),

    path('category<int:id>/', views.PlaceCategoryAPIView.as_view()),
    path('category/', views.PlaceCategoryAPIListView.as_view()),

    path('<int:id>/', views.PlaceAPIView.as_view()),
    path('', views.PlaceAPIListView.as_view()),

    path('gallery/<int:id>/', views.PlaceGalleryAPIView.as_view()),
    path('gallery/', views.PlaceGalleryAPIListView.as_view()),

]
