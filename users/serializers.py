from rest_framework import serializers
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class SignupSerializer(serializers.ModelSerializer):
    refresh = serializers.CharField(read_only=True, source='token')
    access = serializers.CharField(read_only=True, source='token.access_token')

    class Meta:
        model = User
        fields = ('email', 'password', 'refresh', 'access', 'name', 'username')

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        try:
            super().validate(attrs)
        except AuthenticationFailed as ex:
            raise serializers.ValidationError("Incorrect email or password")
        return SignupSerializer(instance=self.user, context=self.context).data
