from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DossierViewSet, RegisterView, MyTokenObtainPairView, MyTokenRefreshView

router = DefaultRouter()
router.register(r'dossiers', DossierViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),   # login
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),  # refresh custom
]
