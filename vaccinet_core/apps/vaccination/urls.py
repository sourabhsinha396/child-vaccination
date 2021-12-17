from django.urls import path

from .views import ping,homepage


urlpatterns = [
    path("ping/", ping, name="ping"),
    path("", homepage, name="homepage"),
]