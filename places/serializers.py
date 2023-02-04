from rest_framework.serializers import ModelSerializer
from places.models import City, PlaceCategory, Place, PlaceGallery, PlaceReview


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class PlaceCategorySerializer(ModelSerializer):

    class Meta:
        model = PlaceCategory
        fields = '__all__'


class PlaceSerializer(ModelSerializer):

    class Meta:
        model = Place
        fields = '__all__'


class PlaceGallerySerializer(ModelSerializer):

    class Meta:
        model = PlaceGallery
        fields = '__all__'


class PlaceReviewSerializer(ModelSerializer):

    class Meta:
        model = PlaceReview
        fields = '__all__'
