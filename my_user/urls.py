from my_user.views import UserCreateView, UserRetrieveUpdateView, UserConfirmViewSet
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('', UserRetrieveUpdateView.as_view(), name='retrieve-update'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

router = DefaultRouter()
router.register(r'confirm', UserConfirmViewSet, basename='confirm')
urlpatterns += router.urls
