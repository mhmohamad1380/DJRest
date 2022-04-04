# main/tasks.py

import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from drf.celery import app


@app.task()
def send_verification_email(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your QuickPublisher account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify', kwargs={'uuid': str(user.verification_uuid)}),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)


# @app.task()
# def send_notification(user_email, user_ip=None):
#     send_mail("Attention", f"Someone has logged into your Account with ip : {user_ip}", "testingappdjango@gmail.com",
#               [user_email], fail_silently=False)
