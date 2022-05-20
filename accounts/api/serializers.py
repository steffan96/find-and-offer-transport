import django.contrib.auth.password_validation as validators
from django.contrib.auth import password_validation
from django.core import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers, status
from rest_framework.response import Response

from accounts.models import CustomUser


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "city", "password", "password2")
        extra_kwargs = {"password": {"write_only": True}, "password2": {"write_only": True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "city")

    # def update(self, instance, validated_data):
    #     instance.email = validated_data['email']
    #     instance.first_name = validated_data['first_name']
    #     instance.last_name = validated_data['last_name']
    #     instance.city = validated_data['city']
    #     instance.save()
    #     return instance


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(
        required=True, write_only=True, validators=[validators.validate_password]
    )

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(_("Neispravna lozinka."))
        return value

    def save(self, **kwargs):
        password = self.validated_data["new_password"]
        user = self.context["request"].user
        user.set_password(password)
        user.save()
        return user

