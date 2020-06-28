from rest_framework import serializers
from django.contrib.auth.models import BaseUserManager
from django.core.validators import validate_email
from django.contrib.auth import get_user_model, password_validation
from rest_framework.authtoken.models import Token
from .models import Profile

User = get_user_model()


class UserLoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=300, required=True)
	password = serializers.CharField(required=True, write_only=True)


class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'


class SuperUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email','is_staff','option')
		depth = 1

	def get_profile(self, instance):
		profil = Profile.objects.create(id=instance.id,option="Free",image="/media/test")
		serializer = ProfileSerializer(profil)
		return serializer.data



class AuthUserSerializer(serializers.ModelSerializer):
	auth_token = serializers.SerializerMethodField()
	class Meta:
		model = User
		fields = ('id', 'username', 'email','first_name',
			'auth_token','last_name','is_active','is_staff')
		read_only_fields = ('id','is_active','is_staff')

	def get_auth_token(self, obj):
		token = Token.objects.create(user=obj)
		return token.key


class EmptySerializer(serializers.Serializer):
	pass


class UserRegisterSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id','first_name','last_name','username','email',
			'password','is_staff','is_superuser')

	def validate_email(self, value):
		user = User.objects.filter(email=value)

		if user:
			raise serializers.ValidationError("Email is already taken")
		return BaseUserManager.normalize_email(value)

	def validate_password(self, value):
		password_validation.validate_password(value)
		return value


class PasswordChangeSerializer(serializers.Serializer):
	current_password = serializers.CharField(required=True)
	new_password = serializers.CharField(required=True)

	def validate_current_password(self, value):

		if not self.context['request'].user.check_password(value):
			raise serializers.ValidationError('Current password does not match')
		return value

	def validate_new_password(self, value):
		password_validation.validate_password(value)
		return value


class EmailChangeSerializer(serializers.Serializer):
	password = serializers.CharField(required=True)
	email = serializers.EmailField(required=True)

	def validate_password(self, value):

		if not self.context['request'].user.check_password(value):
			raise serializers.ValidationError('Current password does not match')
		return value

	def validate_email(self, value):
		user = User.objects.filter(email=value)

		if user:
			raise serializers.ValidationError("Email is already taken")
		return BaseUserManager.normalize_email(value)


class UsernameChangeSerializer(serializers.Serializer):
	password = serializers.CharField(required=True)
	username = serializers.CharField(required=True)

	def validate_password(self, value):

		if not self.context['request'].user.check_password(value):
			raise serializers.ValidationError('Current password does not match')
		return value

	def validate_username(self, value):
		user = User.objects.filter(username=value)

		if user:
			raise serializers.ValidationError("Username is already taken")
		return value

