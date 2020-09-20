from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from my_user.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'email',
            'image',
            'energy',
            'karma',
            'password'
        ]
        read_only_fields = ('energy', 'karma')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])  # get the hashed password
        instance = User.objects.create(**validated_data)  # create a user
        return instance

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':   # and check_password(validated_data['old_password'], instance.password)
                instance.password = make_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        user_profile = UserSerializer(user)
        token['user_profile'] = user_profile.data
        return token