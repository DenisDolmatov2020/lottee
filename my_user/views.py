from django.db import connection
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from my_user.models import Token, User
from number.models import Number
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from my_user.serializers import UserSerializer
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from lottee.settings import EMAIL_HOST_USER
from my_user.tokens import account_activation_token


class UserCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = get_user_model()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # sending confirm to email new user
        token = account_activation_token.make_token(user)
        Token.objects.create(user=user, token=token)
        # site = get_current_site(request)
        html_message = render_to_string('my_user/email_form.html', {
            'title': 'Подтверждение почты',
            'text': 'Нажмите на кнопку для подтвержения аккаунта в приложении Lottee',
            'button_text': 'Подтвердить почту',
            'link': 'http://127.0.0.1:3000/login?page=1&user_id={}&name={}&email={}&token={}'.format(
                user.id, user.name, user.email, token)
        })
        send_mail(
            '{}'.format('Lottee подтверждение почты'),
            # message:
            'CONFIRM EMAIL',
            # from:
            EMAIL_HOST_USER,
            # to:
            [user.email],
            html_message=html_message
        )
        # refresh = RefreshToken.for_user(user) 'refresh': str(refresh), 'access': str(refresh.access_token)}

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )


@csrf_exempt
def user_confirm_email(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        try:
            token = Token.objects.get(user_id=data['user_id'])
        except Token.DoesNotExist:
            token = None

        if token and data['token'] == token.token:
            print('IF')
            token.delete()
            user = User.objects.get(id=data['user_id'])
            user.is_active = True
            user.save()
            return HttpResponse(status=status.HTTP_200_OK)
        else:
            print('ELSE')
            return HttpResponse(status=status.HTTP_226_IM_USED)
    return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserRetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = get_user_model()
    serializer_class = UserSerializer
    # parser_classes = (MultiPartParser,)

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
