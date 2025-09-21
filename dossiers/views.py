from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Dossier
from .serializer import DossierSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .Utils import get_tokens_for_user
# views.py
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenRefreshView
from .serializer import MyTokenRefreshSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class DossierViewSet(viewsets.ModelViewSet):
    queryset = Dossier.objects.all()
    serializer_class = DossierSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'numero'

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if User.objects.filter(username=username).exists():
            return Response({"error": "Utilisateur existe déjà"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "Compte créé"}, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            tokens = get_tokens_for_user(user)
            return Response(tokens)
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

