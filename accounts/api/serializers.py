from rest_framework import serializers
from rest_framework import status
from django.core import exceptions
from rest_framework.response import Response
import django.contrib.auth.password_validation as validators
from accounts.models import CustomUser


class RegisterCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'city', 'password')
        extra_kwargs = {'password': {'write_only':True}}
    
    def validate(self, data):
        user = CustomUser(**data)
        password = data.pop('password', None)
        try:
            validators.validate_password(password=password, user=user) 
        except exceptions.ValidationError as e:
            errors = {}
            errors['password'] = list(e.messages)
            if errors:
                raise serializers.ValidationError(errors)
        return super(RegisterCustomUserSerializer, self).validate(data)

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

    def validate_new_password(self, value):
        validators.validate_password(value)
        return value


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'city')
    
    
    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.city = validated_data['city']
        instance.save()
        return instance

