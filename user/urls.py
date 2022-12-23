from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from user.views import CreateUserView, ManageUserView, ListUserView

urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("login/token-verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("activity/", ListUserView.as_view(), name="activity"),
]

app_name = "user"
