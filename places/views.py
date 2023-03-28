from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from places.models import City, PlaceCategory, Place, PlaceGallery
from places.serializers import CitySerializer, PlaceCategorySerializer, PlaceSerializer, PlaceGallerySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class CityAPIView(generics.GenericAPIView):
    serializer_class = CitySerializer
    authentication_classes = [JWTAuthentication]
    def get(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
            serializer = CitySerializer(item)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response(status=404)


class CityAPIListView(generics.GenericAPIView):
    serializer_class = CitySerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        items = City.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CitySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PlaceCategoryAPIView(generics.GenericAPIView):
    serializer_class = PlaceCategorySerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, id, format=None):
        try:
            item = PlaceCategory.objects.get(pk=id)
            serializer = PlaceCategorySerializer(item)
            return Response(serializer.data)
        except PlaceCategory.DoesNotExist:
            return Response(status=404)


class PlaceCategoryAPIListView(generics.GenericAPIView):
    serializer_class = PlaceCategorySerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        items = PlaceCategory.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceCategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PlaceAPIView(generics.GenericAPIView):
    serializer_class = PlaceSerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, id, format=None):
        try:
            item = Place.objects.get(pk=id)
            serializer = PlaceSerializer(item)
            return Response(serializer.data)
        except Place.DoesNotExist:
            return Response(status=404)


class PlaceAPIListView(generics.GenericAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = PlaceSerializer

    def get(self, request, format=None):
        items = Place.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class PlaceGalleryAPIView(generics.GenericAPIView):
    serializer_class = PlaceGallerySerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, id, format=None):
        try:
            item = PlaceGallery.objects.get(pk=id)
            serializer = PlaceGallerySerializer(item)
            return Response(serializer.data)
        except PlaceGallery.DoesNotExist:
            return Response(status=404)


class PlaceGalleryAPIListView(generics.GenericAPIView):
    serializer_class = PlaceGallerySerializer
    authentication_classes = [JWTAuthentication]

    def get(self, request, format=None):
        items = PlaceGallery.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceGallerySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
