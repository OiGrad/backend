from django.urls import path
from rate.views import rate_place

urlpatterns = [
    path("rate_place", rate_place),
]
