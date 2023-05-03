from rest_framework.serializers import ModelSerializer
from roads.models import PlaceWay ,Road
from places.models import Area
from places.serializers import PlaceSerializer

class AreaSerializer(ModelSerializer):
    class Meta :
        model= Area
        fields = '__all__'

class PlaceWaySerializer(ModelSerializer):
    frm=AreaSerializer()
    to=PlaceSerializer()
    class Meta :
        model= PlaceWay
        fields = '__all__'

class RoadSerializer(ModelSerializer):
    placeWay=PlaceWaySerializer(read_only=True)
    class Meta :
        model= Road
        fields = '__all__'

