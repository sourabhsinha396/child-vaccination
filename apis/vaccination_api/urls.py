from django.urls import path

from .views import (ping,search_parent_by_aadhar,
      get_mother_by_slug,get_child_by_slug, vaccine_list,
      is_child_vaccinated,save_child_vaccination_info,
      save_mother_vaccination_info, update_child_vaccination_info,
      update_mother_vaccination_info,delete_child_vaccination_info,
      delete_mother_vaccination_info,add_parent,update_parent_info,
      add_mother,update_mother_info, add_child, update_child_info,
      is_mother_vaccinated,)

app_name = 'vaccination_api'

urlpatterns = [
    path("ping/", ping, name="ping"),

    path("search-parent/", search_parent_by_aadhar, name="search-parent"),
    path("add-parent/", add_parent, name="add-parent"),
    path("update-parent/<str:slug>/", update_parent_info, name="update-parent"),

    path("get-mother-info/<str:slug>/", get_mother_by_slug, name="search-mother"),
    path("add-mother/", add_mother, name="add-mother"),
    path("update-mother/<str:slug>/", update_mother_info, name="update-mother"),

    path("get-child-info/<str:slug>/", get_child_by_slug, name="search-child"),
    path("add-child/", add_child, name="add-child"),
    path("update-child/<str:slug>/", update_child_info, name="update-child"),

    path("vaccines/", vaccine_list, name="vaccines"),

    path("is-child-vaccinated/<str:slug>/<int:vaccine>/", is_child_vaccinated, name="is-child-vaccinated"),
    path("is-mother-vaccinated/<str:slug>/<int:vaccine>/", is_mother_vaccinated, name="is-mother-vaccinated"),
    
    path("add-child-vaccination-info/", save_child_vaccination_info, name="child-vaccinated"),
    path("add-mother-vaccination-info/", save_mother_vaccination_info, name="mother-vaccinated"),
    path("update-child-vaccination-info/<int:id>", update_child_vaccination_info, name="update-child-vaccinated"),
    path("update-mother-vaccination-info/<int:id>", update_mother_vaccination_info, name="update-mother-vaccinated"),
    path("delete-child-vaccination-info/<int:id>", delete_child_vaccination_info, name="delete-child-vaccinated"),
    path("delete-mother-vaccination-info/<int:id>", delete_mother_vaccination_info, name="delete-mother-vaccinated"),
]