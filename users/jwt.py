from rest_framework_simplejwt.tokens import RefreshToken


def get_token(user):
    token = RefreshToken.for_user(user)
    token["birthdate"] = str(user.birthdate) if user.birthdate else None
    return token