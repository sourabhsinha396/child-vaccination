from django.urls import path

from .views import ping

app_name = 'vaccination_api'

urlpatterns = [
    path("ping/", ping, name="ping"),
]