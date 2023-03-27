from rest_framework.serializers import ModelSerializer

from places.models import City, PlaceCategory, Place, PlaceGallery


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class PlaceCategorySerializer(ModelSerializer):
    class Meta:
        model = PlaceCategory
        fields = '__all__'


class PlaceGallerySerializer(ModelSerializer):
    class Meta:
        model = PlaceGallery
        fields = '__all__'
        

class PlaceSerializer(ModelSerializer):
    city = CitySerializer()
    category = PlaceCategorySerializer()
    gallery = PlaceGallerySerializer(many=True)

    class Meta:
        model = Place
        fields = '__all__'
