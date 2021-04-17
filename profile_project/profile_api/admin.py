from django.contrib import admin
from .models import CustomUser


admin.site.register(CustomUser)



admin.site.index_title='Rest_API_Project'
admin.site.site_title='Admin Page'
admin.site.site_header='Welcome Admin'
