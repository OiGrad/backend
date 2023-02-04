from django.urls import path

from users.views import SignupView, LoginView

app_name = 'users'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),

]
