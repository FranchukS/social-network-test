from django.urls import path

from user.views import CreateUserView


urlpatterns = [
    path("signup/", CreateUserView.as_view(), name="signup"),
]

app_name = "user"
