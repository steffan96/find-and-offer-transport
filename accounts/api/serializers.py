from asyncore import write
from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from accounts.models import CustomUser


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'city', 'password')
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, data):
        password = data.pop('password', None)
        instance = self.Meta.model(**data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ChangePasswordSerializer(serializers.Serializer):
    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
