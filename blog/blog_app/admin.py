from django.contrib import admin
from .models import Blog


# Register your models here.
class B_admin(admin.ModelAdmin):
    list_display = ['title', 'created', 'updated']


admin.site.register(Blog, B_admin)
