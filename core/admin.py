from django.contrib import admin

from core.models import Role, Privilege


# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Privilege)
class PrivilegeAdmin(admin.ModelAdmin):
    list_display = ('privilege_code', 'name',)
