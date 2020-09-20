from django.contrib.auth.models import User
from django.db import connection
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from number.models import Number
from my_user.serializers import UserSerializer
from rest_framework.generics import get_object_or_404, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny,]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response(
            {'user': serializer.data, 'refresh': str(refresh), 'access': str(refresh.access_token)},
            status=status.HTTP_201_CREATED
        )


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        user_numbers = Number.objects.only('lot_id', 'num').filter(owner=request.user)
        numbers_dict = {number.lot_id: number.num for number in user_numbers}
        return Response(
            status=status.HTTP_200_OK,
            data={'user': serializer.data, 'numbers': numbers_dict}
        )

    def partial_update(self, request, *args, **kwargs):
        serializer = UserSerializer(
            instance=request.user,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            status=status.HTTP_200_OK,
            data=serializer.data
        )
