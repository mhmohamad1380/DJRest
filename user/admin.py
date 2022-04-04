from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import signals
from django.urls import reverse
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
