from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers
from api.views import ArticleViewSet, UserViewSet

router = routers.SimpleRouter()
router.register("articles", ArticleViewSet, basename="article")
router.register("users/list", UserViewSet, basename="users")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
    # Auth Token

    path('rest-auth/', include('dj_rest_auth.urls')),
    path('rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('password/reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
        name='account_confirm_email', ),

    # JWT

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
