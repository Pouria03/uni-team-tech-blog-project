from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True,
                                      validators=[validate_password])
    
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'password2')
        extra_kwargs = {
            'full_name': {'required': True},
            'email': {'required': True},
        }
    
    def validate(self, attrs):
        """ check if passwords match """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user