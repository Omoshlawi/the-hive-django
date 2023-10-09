from django.contrib import admin

from stakeholders.models import PropertyOwner, PropertyStaff, Tenant, PropertyStaffRole


# Register your models here.


@admin.register(PropertyOwner)
class PropertyOwnerAdmin(admin.ModelAdmin):
    list_display = ('user', 'surname', 'first-name', 'last_name', 'created_at', 'updated_at')


@admin.register(PropertyStaff)
class PropertyStaffAdmin(admin.ModelAdmin):
    list_display = ('user',  'property', 'created_at', 'updated_at')


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('user',  'unit', 'created_at', 'updated_at')


@admin.register(PropertyStaffRole)
class PropertyStaffRoleAdmin(admin.ModelAdmin):
    list_display = ('staff',  'role', 'created_at', 'updated_at')
