from rest_framework import routers
from .views import CategoryView, SujetView, UserView, RemindViewset

router = routers.DefaultRouter()
router.register(r'category', CategoryView, basename='category')
router.register(r'context', SujetView, basename='context')
router.register(r'user', UserView, basename='user')
router.register(r"category/(?P<id>[0-9]+)/remind", RemindViewset, basename='remind')

urlpatterns = router.urls