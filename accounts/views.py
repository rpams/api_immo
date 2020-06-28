from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, status
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django_filters import rest_framework as filters
from django.contrib.auth import get_user_model, logout
from django.core.exceptions import ImproperlyConfigured
from .utils import get_and_authenticate_user, create_user_account
from . import permissions
from . import models
from . import serializers

User = get_user_model()

# # ------------------------------------------- ProtectedUser
# class ProtectedUserFilter(filters.FilterSet):
# 	# Allows http://api.domain.com/ressource/?name__icontains=value
#     class Meta:
#         model = models.User
#         fields = {
#             'name': ['icontains'],
#             'email': ['icontains', 'exact'],
#         }


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = serializers.EmptySerializer
    serializer_classes = {
        'login': serializers.UserLoginSerializer,
        'register': serializers.UserRegisterSerializer,
        'change_username': serializers.PasswordChangeSerializer,
        'change_email': serializers.EmailChangeSerializer,
        'change_username': serializers.UsernameChangeSerializer,
    }

    @action(methods=['POST', ], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = get_and_authenticate_user(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_200_OK)


    @action(methods=['POST', ], detail=False)
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = create_user_account(**serializer.validated_data)
        data = serializers.AuthUserSerializer(user).data
        return Response(data=data, status=status.HTTP_201_CREATED)


    @action(methods=['POST', ], detail=False)
    def logout(self, request):
        logout(request)
        data = {'success': 'Succesfully logged out'}
        return Response(data=data, status=status.HTTP_200_OK)


    @action(methods=['POST',], detail=False) # permission_classes=[IsAuthenticated]
    def change_password(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(methods=['PUT',], detail=False) # permission_classes=[IsAuthenticated]
    def change_email(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['email'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(methods=['POST',], detail=False) # permission_classes=[IsAuthenticated]
    def change_username(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['username'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def get_serializer_class(self):

        if not isinstance(self.serializer_classes, dict):
            raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

        if self.action in self.serializer_classes.keys():
            return self.serializer_classes[self.action]

        return super().get_serializer_class()


class SuperUserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.SuperUserSerializer
    allowed_methods = ['GET','UPDATE',]

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('name').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)


class SuperUserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.ProfileSerializer
