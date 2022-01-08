from django.urls import path

from .views import ping,search_parent_by_aadhar,get_mother_by_slug,get_child_by_slug

app_name = 'vaccination_api'

urlpatterns = [
    path("ping/", ping, name="ping"),
    path("search-parent/", search_parent_by_aadhar, name="search-parent"),
    path("get-mother-info/<str:slug>/", get_mother_by_slug, name="search-mother"),
    path("get-child-info/<str:slug>/", get_child_by_slug, name="search-child"),
]