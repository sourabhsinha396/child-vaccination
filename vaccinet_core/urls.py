from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('browsable-apis/', include('rest_framework.urls')),
    path('api/', include('apis.vaccination_api.urls')),
    path('', include('apps.vaccination.urls')),
    path('', include('apps.accounts.urls')),
]
