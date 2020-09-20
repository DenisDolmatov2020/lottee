from django.urls import path
from my_user.views import UserCreateView, UserRetrieveUpdateView, MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    path('', UserRetrieveUpdateView.as_view(), name='retrieve-update'),
    path('token/', MyTokenObtainPairView.as_view(), name='token'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]
