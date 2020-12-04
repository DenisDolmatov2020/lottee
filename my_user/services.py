from my_user.models import Token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from lottee.settings import EMAIL_HOST_USER
from my_user.tokens import account_activation_token


def send_confirm(user):
    token = account_activation_token.make_token(user)
    Token.objects.create(user=user, token=token)
    # sending confirm to email new user
    html_message = render_to_string('my_user/email_form.html', {
        'title': 'Подтверждение почты',
        'text': 'Нажмите на кнопку для подтвержения аккаунта в приложении Lottee',
        'button_text': 'Подтвердить почту',
        'link': 'http://127.0.0.1:3000/auth?page=1&user_id={}&name={}&email={}&token={}'.format(
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
