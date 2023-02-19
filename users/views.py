from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, RetrieveDestroyAPIView, ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import permissions


from .models import User
from places.models import Place
from .serializers import SignupSerializer, LoginSerializer,AddFavoritePlaceSerializer
from places.serializers import PlaceSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username__iexact=request.data.get('username', ''))
        return self.create(request, *args, **kwargs)


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer


class FavoritePlaceView(RetrieveAPIView):
    permission_classes  = [permissions.IsAuthenticated] 
    serializer_class    = PlaceSerializer       
    query_set = []
    def get(self, request, *args, **kwargs):
        query_set = Place.objects.filter(user=request.user).all()
        serializer = PlaceSerializer(query_set,many=True)
        return Response(serializer.data)
    


class AddFavoritePlaceView(CreateAPIView):
    serializer_class = AddFavoritePlaceSerializer
    permission_classes  = [permissions.IsAuthenticated] 

    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        new_place = Place.objects.get(pk=id)
        request.user.favorite_places.add(new_place)
        query_set = Place.objects.filter(user=request.user).all()
        serializer = PlaceSerializer(query_set,many=True)
        return Response(serializer.data)