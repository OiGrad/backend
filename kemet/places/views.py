from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from places.serializers import CitySerializer, PlaceCategorySerializer, PlaceSerializer, PlaceGallerySerializer, PlaceReviewSerializer
from places.models import City, PlaceCategory, Place, PlaceGallery, PlaceReview




class CityAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
            serializer = CitySerializer(item)
            return Response(serializer.data)
        except City.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
        except City.DoesNotExist:
            return Response(status=404)
        serializer = CitySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = City.objects.get(pk=id)
        except City.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class CityAPIListView(APIView):

    def get(self, request, format=None):
        items = City.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = CitySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PlaceCategoryAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PlaceCategory.objects.get(pk=id)
            serializer = PlaceCategorySerializer(item)
            return Response(serializer.data)
        except PlaceCategory.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PlaceCategory.objects.get(pk=id)
        except PlaceCategory.DoesNotExist:
            return Response(status=404)
        serializer = PlaceCategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PlaceCategory.objects.get(pk=id)
        except PlaceCategory.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlaceCategoryAPIListView(APIView):

    def get(self, request, format=None):
        items = PlaceCategory.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceCategorySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PlaceAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Place.objects.get(pk=id)
            serializer = PlaceSerializer(item)
            return Response(serializer.data)
        except Place.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Place.objects.get(pk=id)
        except Place.DoesNotExist:
            return Response(status=404)
        serializer = PlaceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Place.objects.get(pk=id)
        except Place.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlaceAPIListView(APIView):

    def get(self, request, format=None):
        items = Place.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PlaceGalleryAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PlaceGallery.objects.get(pk=id)
            serializer = PlaceGallerySerializer(item)
            return Response(serializer.data)
        except PlaceGallery.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PlaceGallery.objects.get(pk=id)
        except PlaceGallery.DoesNotExist:
            return Response(status=404)
        serializer = PlaceGallerySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PlaceGallery.objects.get(pk=id)
        except PlaceGallery.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlaceGalleryAPIListView(APIView):

    def get(self, request, format=None):
        items = PlaceGallery.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceGallerySerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceGallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PlaceReviewAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = PlaceReview.objects.get(pk=id)
            serializer = PlaceReviewSerializer(item)
            return Response(serializer.data)
        except PlaceReview.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = PlaceReview.objects.get(pk=id)
        except PlaceReview.DoesNotExist:
            return Response(status=404)
        serializer = PlaceReviewSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = PlaceReview.objects.get(pk=id)
        except PlaceReview.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PlaceReviewAPIListView(APIView):

    def get(self, request, format=None):
        items = PlaceReview.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PlaceReviewSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PlaceReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
