from background_task import background

from django.core.mail import send_mail
from django.db.models.signals import pre_save, post_save
from rest_framework.exceptions import ParseError
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from api.permissions import *
from api.serializers import ArticleSerializer, UserSerializer, AuthorSerializer
from blog.models import Article
from django.contrib.auth import get_user_model
from django.dispatch import receiver


class UserViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsSuperUser]


class ArticleViewSet(ModelViewSet):
    parser_classes = [JSONParser]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ['author__username', 'publish']
    search_fields = ['title', 'content', 'author__username', 'author__first_name', 'author__last_name']
    ordering_fields = ["publish", "created"]

    def get_permissions(self):

        if self.action in ["retrieve", "put", "delete"]:
            self.permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        else:
            self.permission_classes = [IsStaffOrReadOnly]
        return [permission() for permission in self.permission_classes]



# class ArticleApiList(ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleCreateApiList(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleOther(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]


# class UserApiList(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUser]
#
#
# class UserOther(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsSuperUser]

# class UserCreateApiList(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
