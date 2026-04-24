from django.contrib import admin
from django.urls import path, include

from users.views import RegisterView, LoginView, GoogleLoginView, VerifyCodeView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('google-login/', GoogleLoginView.as_view()),
    path('verify-code/', VerifyCodeView.as_view()),

    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    path('products/', include('products.urls')),

    path('swagger/', schema_view.with_ui('swagger')),
]