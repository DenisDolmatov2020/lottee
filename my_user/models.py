from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from lottee.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = 'RESET PASSWORD'
    # "<a>{}?token={}</a>".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    html_message = render_to_string('my_user/email_form.html', {
        'title': 'Сброс пароля',
        'text': 'Нажмите на кнопку сбросить пароль или перейдите по ссылке',
        'button_text': 'Сбросить пароль',
        'link': 'http://127.0.0.1:3000/login?page=3&token={}'.format(reset_password_token.key)
    })
    send_mail(
        # title:
        "{title}".format(title="Lottee сброс пароля"),
        # message:
        email_plaintext_message,
        # from:
        EMAIL_HOST_USER,
        # to:
        [reset_password_token.user.email],
        html_message=html_message
    )


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            # email = 'admin@lottee.com'
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('locale', 'ru')
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('locale', 'en')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """ User model """
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(verbose_name='name', max_length=255)
    phone = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=200, null=True)
    image = models.ImageField(verbose_name='Аватар', upload_to='user/', blank=True, null=True)

    locale = models.CharField(verbose_name='Локация', max_length=16, default='ru')
    language = models.CharField(verbose_name='Язык системы', max_length=16, default='ru')
    energy = models.PositiveSmallIntegerField(verbose_name='Энергия', default=15)
    karma = models.SmallIntegerField(verbose_name='Карма пользователя', default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = UserManager()

    def __str__(self):
        return self.email


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)


@receiver(pre_save, sender=User)
def set_new_user_inactive(sender, instance, **kwargs):
    if instance._state.adding is True:
        print('Creating Inactive User')
        instance.is_active = False
        print('INSTANCE')
        print(instance)
    else:
        print('Updating User Record')

