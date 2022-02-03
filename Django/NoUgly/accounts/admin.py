from django.contrib import admin
from .models import *

@admin.register(User)# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 10