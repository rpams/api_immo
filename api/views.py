from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.decorators import action, api_view
from django.views.decorators.csrf import csrf_exempt
from . import serializers
from . import models
from django_filters import rest_framework as filters
from . import permissions


# ------------------------------------------- service_immobilier
class ServiceImmobilierFilter(filters.FilterSet):
	# Allows http://api.domain.com/ressource/?username__icontains=value
    class Meta:
        model = models.ServiceImmobilier
        fields = {
            'title': ['icontains'],
            'description': ['icontains'],
			'price': ['lte', 'gte', 'exact'],
			'coordinate': ['icontains']
        }

class ServiceImmobilierView(viewsets.ModelViewSet):
	queryset = models.ServiceImmobilier.objects.all()
	serializer_class = serializers.ServiceImmobilierSerializer
	filterset_class = ServiceImmobilierFilter
	pagination_class = PageNumberPagination

	def perform_create(self, serializer):
		publisher = self.request.user
		if publisher.profile.is_creator:
			serializer.save()
		else:
			raise PermissionDenied("Vous n'êtes pas autorisé. Passez en prémium")

	def perform_destroy(self, serializer):
		anounce_instance = self.get_object()
		user = self.request.user
		publisher = anounce_instance.publisher

		if user != publisher:
			raise ValidationError("Vous n'êtes pas autorisé !")


	@csrf_exempt
	@action(methods=['get'], detail=False)
	def newest(self, request):
		newest = self.get_queryset().order_by('title').last()
		serializer = self.get_serializer_class()(newest)
		return Response(serializer.data)


# ------------------------------------------- CategoryImmobilier
class CategoryImmobilierFilter(filters.FilterSet):
	# Allows http://api.domain.com/ressource/?category__icontains=value
    class Meta:
        model = models.CategoryImmobilier
        fields = {
            'category': ['icontains', 'exact'],
        }

class CategoryImmobilierView(viewsets.ModelViewSet):
	queryset = models.CategoryImmobilier.objects.all()
	serializer_class = serializers.CategoryImmobilierSerializer
	filterset_class = CategoryImmobilierFilter
	pagination_class = PageNumberPagination

	def perform_create(self, serializer):
		category_pk=self.kwargs.get("category_pk")
		category_instance=generics.get_object_or_404(Event,pk=category_pk)
		category_queryset=Reviews.objects.filter(Event=category_instance,reviewer=reviewer)

		if category_queryset.exists():
			raise ValidationError("oops already created,Try editing")
		serializer.save(category=category_instance)

	@csrf_exempt
	@action(methods=['get'], detail=False)
	def newest(self, request):
		newest = self.get_queryset().order_by('category').last()
		serializer = self.get_serializer_class()(newest)
		return Response(serializer.data)



# ------------------------------------------- PriceNature
class PriceNatureFilter(filters.FilterSet):
	# Allows http://api.domain.com/ressource/?price_nature__icontains=value
    class Meta:
        model = models.PriceNature
        fields = {
            'price_nature': ['icontains', 'exact'],
        }

class PriceNatureView(viewsets.ModelViewSet):
	queryset = models.PriceNature.objects.all()
	serializer_class = serializers.PriceNatureSerializer
	filterset_class = PriceNatureFilter
	pagination_class = PageNumberPagination

	@csrf_exempt
	@action(methods=['get'], detail=False)
	def newest(self, request):
		newest = self.get_queryset().order_by('price_nature').last()
		serializer = self.get_serializer_class()(newest)
		return Response(serializer.data)
