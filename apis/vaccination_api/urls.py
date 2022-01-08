from django.urls import path

from .views import ping,search_parent_by_aadhar

app_name = 'vaccination_api'

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("search_parent/", search_parent_by_aadhar, name="search-parent"),
]