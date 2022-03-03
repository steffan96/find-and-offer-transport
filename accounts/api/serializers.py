from rest_framework import serializers
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


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'city')
    
    def validate_email(self, value):
        user = self.context['request'].user
        if CustomUser.objects.exclude(
            pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({
                "email": "Korisnik sa ovom email adresom već postoji."})
        return value

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.city = validated_data['city']
        instance.save()
        return instance

