from django.core.cache import cache
import random

CODE_TTL = 300  # 5 минут


def generate_code():
    return str(random.randint(100000, 999999))


def get_key(user_id):
    return f"confirm_code_{user_id}"


def save_code(user_id):
    code = generate_code()
    cache.set(get_key(user_id), code, timeout=CODE_TTL)
    return code


def verify_code(user_id, input_code):
    key = get_key(user_id)
    saved_code = cache.get(key)

    if not saved_code:
        return False

    if saved_code == input_code:
        cache.delete(key)  # удаляем после использования
        return True

    return False