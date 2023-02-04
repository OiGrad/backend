from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateAPIView, \
    RetrieveAPIView, RetrieveDestroyAPIView, ListAPIView, ListCreateAPIView, DestroyAPIView, UpdateAPIView, \
    RetrieveUpdateDestroyAPIView

from .models import User
from .serializers import SignupSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class SignupView(CreateAPIView):
    serializer_class = SignupSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(username__iexact=request.data.get('username', ''))
        return self.create(request, *args, **kwargs)

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
