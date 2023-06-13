from rest_framework.serializers import ModelSerializer
from fav.models import FavPlaces
from places.serializers import PlaceSerializer
from users.serializers import UserSerializer


class FavPlaceSerializers(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = FavPlaces
        fields = ("id", "user", "place")
