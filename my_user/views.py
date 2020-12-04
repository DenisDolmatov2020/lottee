from django.db import connection
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from my_user.serializers import TokenSerializer, UpdatePasswordSerializer
from my_user.models import Token, User
from my_user.services import send_confirm
from number.models import Number
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from my_user.serializers import UserSerializer


class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        send_confirm(user)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


class UpdatePasswordView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdatePasswordSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)


class UserConfirmViewSet(ViewSet):
    permission_classes = [AllowAny]
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

    @staticmethod
    def get_object_or_none(obj, **kwargs):
        try:
            return obj.objects.get(**kwargs)
        except obj.DoesNotExist:
            return None

    # подтверждение почты
    def create(self, request):
        data = JSONParser().parse(request)
        user = self.get_object_or_none(User, pk=data['user_id'])
        token = self.get_object_or_none(Token, user_id=data['user_id'])
        if token and data['token'] == token.token:
            token.delete()
            user.is_active = True
            user.save()

        if user.is_active:
            return Response({'message': 'Почта подтверждена, войдите'}, status=status.HTTP_200_OK)
        return Response({'message': 'Токен устарел или не верен'}, status=status.HTTP_408_REQUEST_TIMEOUT)

    # Повторная отправка подтверждения или проверка статуса регистрации почты
    def patch(self, request):
        data = JSONParser().parse(request)
        user = self.get_object_or_none(User, email=data['email'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif user.is_active:
            return Response(status=status.HTTP_200_OK)

        token = self.get_object_or_none(Token, user=user)
        if token:
            token.delete()
        send_confirm(user)
        return Response(status=status.HTTP_201_CREATED)

    # Проверка статуса регистрации почты
    def put(self, request):
        data = JSONParser().parse(request)
        user = self.get_object_or_none(User, email=data['email'])
        if user and not user.is_active:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        user_numbers = Number.objects.filter(user=request.user)
        data_ = serializer.data
        data_['numbers'] = {number.lot_id: number.num for number in user_numbers}
        data_['prize_count'] = user_numbers.filter(won=True).count()
        print('Total requests count: %s' % len(connection.queries))
        return Response(
            status=status.HTTP_200_OK,
            data={'user': data_}
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
