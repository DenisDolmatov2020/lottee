from django.urls import path
from my_user.views import UserCreateView, UserRetrieveUpdateView, user_confirm_email
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.urls import path, include

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('confirm-email/', user_confirm_email),
    path('', UserRetrieveUpdateView.as_view(), name='retrieve-update'),
    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
