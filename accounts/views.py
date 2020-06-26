from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django_filters import rest_framework as filters
from . import permissions
from . import models
from . import serializers



# # ------------------------------------------- ProtectedUser
# class ProtectedUserFilter(filters.FilterSet):
# 	# Allows http://api.domain.com/ressource/?name__icontains=value
#     class Meta:
#         model = models.User
#         fields = {
#             'name': ['icontains'],
#             'email': ['icontains', 'exact'],
#         }
# # ------------------------------------------- User
# class UserFilter(filters.FilterSet):
# 	# Allows http://api.domain.com/ressource/?name__icontains=value
#     class Meta:
#         model = models.User
#         fields = {
#             'name': ['icontains'],
#             'email': ['icontains', 'exact'],
# 			'number': ['icontains'],
# 			'option': ['icontains']
#         }


class UserProfileListCreateView(ListCreateAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    pagination_class = PageNumberPagination
    # filterset_class = UserFilter
    parser_classes = (MultiPartParser, FormParser,)
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self, *args, **kwargs):
    #     qs = super(models.UserProfile, self).get_queryset(*args, **kwargs)
    #     return qs

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('name').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
    

# ------------------------------------------- User
class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    pagination_class = PageNumberPagination
    # filterset_class = ProtectedUserFilter
    parser_classes = (MultiPartParser, FormParser,)
    # permission_classes = [IsOwnerProfileOrReadOnly,IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        qs = super(models.UserProfile, self).get_queryset(*args, **kwargs)
        # qs = qs.filter(owner=self.request.user)
        print(qs[0].file)

        return qs

    @csrf_exempt
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('name').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

    @csrf_exempt
    @action(detail=True, url_path='remind', methods=['get'])
    def remind_single(self, request, *args, **kwargs):
        user = self.get_object()
        send_mail(
			subject=f"Reset password : {user.name}",
			message=f"You need to reset your password {user.name}",
			from_email="site@domain.com",
			recipient_list=[user.email],
			fail_silently=False)
        output = {'name' : user.name, 'email' : user.email, 'state' : 'Email sent'}
        return Response(output)

