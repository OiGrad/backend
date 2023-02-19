from django.urls import path

from users.views import SignupView, LoginView,FavoritePlaceView,AddFavoritePlaceView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('favorite-places/', FavoritePlaceView.as_view(), name='favorite-places'),
    path('add-favorite-places/', AddFavoritePlaceView.as_view(), name='favorite-places'),

]
