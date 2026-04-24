from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def log_user_registration(user_id):
    user = User.objects.get(id=user_id)
    print(f"[CELERY] Пользователь зарегистрирован: {user.email}")



@shared_task
def cleanup_inactive_users():
    users = User.objects.filter(is_active=False)
    count = users.count()
    users.delete()
    print(f"[CELERY] Удалено неактивных пользователей: {count}")


@shared_task
def send_email_task(user_id):
    user = User.objects.get(id=user_id)

    send_mail(
        subject="Добро пожаловать",
        message="Спасибо за регистрацию!",
        from_email="test@gmail.com",
        recipient_list=[user.email],
        fail_silently=True,
    )