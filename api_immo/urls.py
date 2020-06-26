from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from .views import login

schema_view = get_swagger_view(title='API Documentation')


API_TITLE = 'IMMO SEJOUR API'
API_DES = 'API Documentation'

urlpatterns = [
    path('', schema_view),
	# path('',include_docs_urls(title=API_TITLE, description=API_DES), name="documentation"),
    path('admin/', admin.site.urls, name="admin"),
    path('api/services/', include('api.urls'), name="api_root"),
    path('api/profiles/', include('accounts.urls')),
    path('api/login', login, name='login'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/docs/', include_docs_urls(title=API_TITLE, description=API_DES), name="docs"),
    # path('api/token/', jwt.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path('api/token/refresh/', jwt.TokenRefreshView.as_view(), name="token_refresh"),
    # path('api/token/verify/', jwt.TokenVerifyView.as_view(), name='token_verify')
]