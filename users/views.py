from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegisterSerializer
from .google_auth import google_auth


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    pass


class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("access_token")
        user = google_auth(token)
        return Response({"email": user.email})