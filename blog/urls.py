from django.urls import path

from blog import views

urlpatterns = [
    path('', views.ArticleView.as_view()),
    path('articles/<slug:slug>/<int:pk>', views.ArticleDetail.as_view(), name="article_detail"),
]
