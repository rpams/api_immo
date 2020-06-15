from rest_framework import serializers
from .models import Category, Sujet, User

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id', 'category', 'sous_category')


class SujetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sujet
		fields = ('id', 'name', 'context', 'ville', 'coordonnees')


class UserSerializer(serializers.ModelSerializer):
	owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'sujet', 'owner', 'date')
