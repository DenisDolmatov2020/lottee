from django.urls import path
from my_user.views import UserCreateView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
]
