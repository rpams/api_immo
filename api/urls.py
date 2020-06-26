from rest_framework import routers
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import ServiceImmobilierView, CategoryImmobilierView
from .views import PriceNatureView

router = routers.DefaultRouter()
router.register(r'immobilier/category', CategoryImmobilierView, basename='category-immobilier')
router.register(r'immobilier', ServiceImmobilierView, basename='service-immobilier')
router.register(r'price-nature', PriceNatureView, basename='nature-price')

urlpatterns = [
	path('', include(router.urls)),
	# path('immobilier/', ServiceImmobilierView.as_view(), name='service-immobilier'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)