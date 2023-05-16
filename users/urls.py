from django.urls import path

from users.views import (
    SignupView,
    LoginView,
    FavoritePlaceView,
    AddFavoritePlaceView,
    GetUserInfo,
    make_it_super_user,
)

app_name = "users"

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("singin/", LoginView.as_view(), name="login"),
    path("favorite-places/", FavoritePlaceView.as_view(), name="favorite-places"),
    path(
        "add-favorite-places/", AddFavoritePlaceView.as_view(), name="favorite-places"
    ),
    path("get-user-date", GetUserInfo, name="get-user"),
    path("make-it_superuser", make_it_super_user),
]
