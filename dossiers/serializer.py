from rest_framework import serializers
from .models import Dossier
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    username = serializers.CharField(read_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh_token_str = attrs['refresh']
        refresh = RefreshToken(refresh_token_str)
        # Ajouter le username dans l'access token
        access = refresh.access_token
        access['username'] = refresh['username']  # récupère depuis le token initial
        data['access'] = str(access)
        data['username'] = access['username']
        return data

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Ajouter le username dans le token d'accès
        token['username'] = user.username
        return token

class DossierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dossier
        fields = '__all__'
