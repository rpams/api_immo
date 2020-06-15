from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt
from rest_framework.documentation import include_docs_urls

API_TITLE = 'IMMO SEJOUR API'
API_DESCRIPTION = 'API Documentation'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/docs/',include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api/token/', jwt.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('api/token/refresh/', jwt.TokenRefreshView.as_view(), name="token_refresh"),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]
