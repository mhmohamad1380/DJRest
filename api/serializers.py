from rest_framework import serializers
from django.contrib.auth import get_user_model
from blog.models import Article
import html2text


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name"]


class ArticleSerializer(serializers.ModelSerializer):
    def get_author(self, obj):
        return {
            "username": obj.author.username,
            "first_name": obj.author.first_name,
            "last_name": obj.author.last_name,
            "id": obj.author.id,
            "last login": obj.author.last_login,
        }

    def get_content(self, obj):
        return {
            "content": html2text.html2text(obj.content)
        }

    author = serializers.SerializerMethodField("get_author")
    content = serializers.SerializerMethodField("get_content")

    class Meta:
        model = Article
        exclude = ['created']

    def validate_title(self, value):
        filter_titles = ['javascript', 'js', 'PHP', 'laravel', 'C#']

        for i in filter_titles:
            if i in value:
                raise serializers.ValidationError("You can't use this words!! : {}".format(filter_titles))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"
