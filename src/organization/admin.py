from django.contrib import admin
from organization.models import Organization


@admin.register(Organization)
class UserAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name')
