from django.contrib.auth.hashers import make_password, check_password
from rest_framework import serializers
from my_user.models import User, Token
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _
from my_user.services import send_confirm


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'address',
            'image',
            'energy',
            'karma',
            'password',
            'old_password'
        ]
        read_only_fields = ('energy', 'karma')
        extra_kwargs = {'password': {'write_only': True}, 'old_password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # get the hashed password
        instance = User.objects.create(**validated_data)  # create a user

        return instance

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password' and check_password(validated_data['old_password'], instance.password):
                instance.password = make_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance


class UpdatePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=128, write_only=True, required=True)
    password = serializers.CharField(max_length=128, write_only=True, required=True)
    repeat_password = serializers.CharField(max_length=128, write_only=True, required=True)

    def validate(self, data):
        if data['password'] != data['repeat_password']:
            raise serializers.ValidationError({'message': _('Пароли не совпадают.')})
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({'message':
                                               [_('Некорректно введен старый пароль.'),  _('Пароли не совпадают.')]})
        password_validation.validate_password(data['password'], user)
        return data

    def save(self, **kwargs):
        password = self.validated_data['password']
        user = self.context['request'].user
        user.set_password(password)
        user.save()
        return user
