

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('profile_api.urls'))
]


# admin.site.index_title='Rest_API_Project'
# admin.site.site_title='Admin Page'
# admin.site.site_header='Welcome Admin'