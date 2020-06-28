from rest_framework import routers
from django.urls import path, include
from .views import AuthViewSet, SuperUserListView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter(trailing_slash=False)
router.register("profiles", AuthViewSet, basename="action-profiles")
router.register("list", SuperUserListView, basename="profiles")
router.register("all-list", SuperUserListView, basename="profile")
# router.register("user/<int:pk>", UserProfileDetailView, basename='user')

urlpatterns = router.urls

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)