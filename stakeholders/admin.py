from django.contrib import admin

from stakeholders.models import PropertyOwner, PropertyStaff, Tenant, PropertyStaffRole, Person


# Register your models here.


@admin.register(PropertyOwner)
class PropertyOwnerAdmin(admin.ModelAdmin):
    list_display = ('person', 'created_at', 'updated_at')


@admin.register(PropertyStaff)
class PropertyStaffAdmin(admin.ModelAdmin):
    list_display = ('person', 'property', 'created_at', 'updated_at')


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('person', 'unit', 'created_at', 'updated_at')


@admin.register(PropertyStaffRole)
class PropertyStaffRoleAdmin(admin.ModelAdmin):
    list_display = ('staff', 'role', 'created_at', 'updated_at')


@admin.register(Person)
class PropertyStaffRoleAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'surname', 'first_name', 'last_name', 'phone_number', 'date_of_birth', 'gender',)
