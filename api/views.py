# from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Category, Sujet, User
from .serializers import CategorySerializer, SujetSerializer, UserSerializer
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .permissions import IsOwner
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from hedju import HeaderLimitOffsetPagination

# ------------------------------------------- Category
class CategoryFilter(filters.FilterSet):
	# Allows http://api.domain.com/ressource/?category=value
    class Meta:
        model = Category
        fields = {
            'category': ['icontains', 'exact'],
            'sous_category': ['icontains']
        }

class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all().order_by('category')
	serializer_class = CategorySerializer
	filterset_class = CategoryFilter
	# Allows http://api.domain.com/ressource/?page=value
	pagination_class = PageNumberPagination


# ------------------------------------------- Context
class UserFilter(filters.FilterSet):
	# Allows http://api.domain.com/ressource/?username=value
    class Meta:
        model = Sujet
        fields = {
            'name': ['icontains'],
            'ville': ['icontains'],
            'description': ['icontains'],
            'coordonnees': ['icontains']
        }

class SujetView(viewsets.ModelViewSet):
	permission_classes = [IsOwner]
	queryset = Sujet.objects.all()
	serializer_class = SujetSerializer
	pagination_class = PageNumberPagination




# ------------------------------------------- User
class UserFilter(filters.FilterSet):
	# Allows http://api.domain.com/ressource/?username=value
    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'email': ['icontains']
        }

class UserView(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	# authentication_classes = (TokenAuthentication,)
	queryset = User.objects.all().order_by("username")
	serializer_class = UserSerializer
	filterset_class = UserFilter
	pagination_class = PageNumberPagination

	@action(methods=['get'], detail=False)
	def newest(self, request):
		newest = self.get_queryset().order_by('username').last()
		serializer = self.get_serializer_class()(newest)
		return Response(serializer.data)




# ------------------------------------------- Reminder
class RemindViewset(viewsets.ModelViewSet):
	queryset = Category.objects.all().order_by('category')
	serializer_class = CategorySerializer
	@action(detail=True, url_path='remind', methods=['post'])
	def remind_single(self, request, *args, **kwargs):
		obj = self.get_object()
		send_mail(
			subject=f"Reset password : {obj.what.name}",
			message=f"You need to reset your password {obj.what.name}",
			from_mail="site@domain.com",
			recipient_list=[objto_who.email],
			fail_silently=False)
		return Response("Email sent.")