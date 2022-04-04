from django.contrib.auth import get_user_model
from django.db.models import Q
from django.db.models.signals import pre_save
from django.dispatch import receiver
import json
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView

from api.serializers import AuthorSerializer
from blog.models import Article


class ArticleView(ListView):
    template_name = 'index.html'
    context_object_name = "Articles"

    def get_queryset(self):
        queryset = Article.objects.filter(publish=True)
        search = self.request.GET.get("search")
        if search is not None:
            lookup = (Q(title__icontains=search) | Q(content__icontains=search) | Q(
                author__username__icontains=search) | Q(author__first_name__icontains=search) | Q(
                author__last_name__icontains=search))
            queryset = queryset.filter(lookup)
        return queryset


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    context_object_name = "Article"

    def get_object(self, queryset=None):
        return get_object_or_404(
            Article.objects.filter(publish=True),
            pk=self.kwargs.get("pk"),
            slug=self.kwargs.get("slug"),
        )
