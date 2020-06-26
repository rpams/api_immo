from rest_framework import routers
from django.urls import path, include
from .views import UserProfileListCreateView, UserProfileDetailView
from django.conf import settings
from django.conf.urls.static import static


# router = routers.DefaultRouter()
# router.register("users", UserProfileListCreateView)
# router.register("user/<int:pk>", UserProfileDetailView, basename='user')


urlpatterns = [
	# path("", include(router.urls)),
    path("users", UserProfileListCreateView.as_view(),name="all-profiles"),
    path("user/<int:pk>", UserProfileDetailView.as_view(),name="profile")
    # path("",include(router.urls))
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)