from rest_framework.exceptions import ValidationError
from datetime import date


def validate_age(request):
    birthdate = request.auth.get("birthdate")

    if not birthdate:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")

    year = int(birthdate.split("-")[0])
    age = date.today().year - year

    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")