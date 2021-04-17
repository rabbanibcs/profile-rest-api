

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


# admin.site.index_title='Rest_API_Project'
# admin.site.site_title='Admin Page'
# admin.site.site_header='Welcome Admin'