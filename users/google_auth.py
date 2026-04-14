import requests
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from .models import CustomUser


def google_auth(access_token):
    response = requests.get(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    )

    data = response.json()

    email = data.get("email")
    if not email:
        raise ValidationError("Google не вернул email")

    user, _ = CustomUser.objects.get_or_create(email=email)

    user.first_name = data.get("given_name", "")
    user.last_name = data.get("family_name", "")
    user.is_active = True
    user.last_login = timezone.now()
    user.registration_source = "google"
    user.save()

    return user