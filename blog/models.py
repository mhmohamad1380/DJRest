from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True)
    slug = models.SlugField(blank=False, null=True)
    author = models.ForeignKey(get_user_model(), null=True, blank=False, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image", null=True)
    content = HTMLField(null=True, blank=False)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
