from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     fields = ['display_name', 'description']
#     exclude = ['description']
#     list_display = ['display_name']
#     list_filter = ['display_name',]
#     search_fields = ['display_name']