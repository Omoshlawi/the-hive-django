from django.contrib import admin

from properties.models import PropertyType, PropertyStatus, Property, PropertyImage, PropertyUnit, PropertyUnitImage


# Register your models here.


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon_name')


@admin.register(PropertyStatus)
class PropertyStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status_code')


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zipcode', 'created_at', 'update_at')


@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'is_primary', 'created_at', 'update_at')


@admin.register(PropertyUnit)
class PropertyUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'price', 'created_at', 'update_at')


@admin.register(PropertyUnitImage)
class PropertyUnitImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'is_primary', 'created_at', 'update_at')
