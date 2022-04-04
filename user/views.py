from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import signals
from django.dispatch import receiver
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from user.models import User

from django.db.models import signals
from drf.tasks import send_verification_email


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.pk)


signals.pre_save.connect(user_post_save, sender=User)


# def send_email(sender, instance,*args,**kwargs):
#     send_notification(instance.email)
#     print(instance.email)
#     print(sender)
#
#
# signals..connect(send_email, sender=User)


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()

    return redirect('/')
