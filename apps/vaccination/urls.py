from django.urls import path

from .views import ping,homepage,contact_us

app_name = 'vaccination'

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("", homepage, name="homepage"),
    path("contact/", contact_us, name="contact_us"),
]