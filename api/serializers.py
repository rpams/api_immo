from rest_framework import serializers
from .models import AnnonceurImmobilier, ContracteurImmobilier
from .models import ServiceImmobilier, ImageAnnonceImmobilier
from .models import CategoryImmobilier, PriceNature, ContracteurImmobilier
import os

# ------------------------------------------- ImageAnnonce
class ImageAnnonceSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImageAnnonceImmobilier
		fields = '__all__'

# ------------------------------------------- PriceNature <-
class PriceNatureSerializer(serializers.ModelSerializer):
	class Meta:
		model = PriceNature
		fields = ('pk', 'price_nature')

# ------------------------------------------- CategoryImmobilier <-
class CategoryImmobilierSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryImmobilier
		fields = ('pk', 'category')



# ---------------------------------------------------------------#
# ------------------------------------------- ServiceImmobilier <-
class ServiceImmobilierSerializer(serializers.ModelSerializer):
	# Modifier avec PrimaryKeyRelatedField(read_only=True) ou JSONFielf si souci
	image = ImageAnnonceSerializer()
	publisher = serializers.StringRelatedField(read_only=True)
	cateroy = CategoryImmobilierSerializer()
	price_nature = PriceNatureSerializer()
	class Meta:
		model = ServiceImmobilier
		fields = '__all__'

# ------------------------------------------- ServiceImmo <-
class ServiceImmoSerializer(serializers.ModelSerializer):
	coordinate = serializers.JSONField()
	class Meta:
		model = ServiceImmobilier
		fields = ('title','image','coordinate','price')


# ------------------------------------------- AnnonceurImmobilier <-
class AnnonceurImmobilierSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=True)
	annonce = serializers.StringRelatedField(read_only=True)
	class Meta:
		model = AnnonceurImmobilier
		fields = '__all__'

# ------------------------------------------- ContracteurImmobilier <-
class ContracteurImmobilierSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(read_only=True)
	annonce = serializers.StringRelatedField(read_only=True)
	class Meta:
		model = ContracteurImmobilier
		fields = '__all__'