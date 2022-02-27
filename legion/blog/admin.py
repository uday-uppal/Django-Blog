from django.contrib import admin

# Register your models here.
# admin.register.site()
from .models import BlogModel,contact_model
admin.site.register(BlogModel)
admin.site.register(contact_model)
