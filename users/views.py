from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer
from .google_auth import google_auth
from .utils import save_code, verify_code


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        code = save_code(user.id)

        print("CONFIRM CODE:", code)  # вместо SMS/email


class LoginView(TokenObtainPairView):
    pass


class GoogleLoginView(APIView):
    def post(self, request):
        token = request.data.get("access_token")
        user = google_auth(token)
        return Response({"email": user.email})


class VerifyCodeView(APIView):
    def post(self, request):
        user_id = request.data.get("user_id")
        code = request.data.get("code")

        if verify_code(user_id, code):
            return Response({"message": "Код подтвержден"})

        return Response(
            {"error": "Неверный или истёк код"},
            status=status.HTTP_400_BAD_REQUEST
        )
    