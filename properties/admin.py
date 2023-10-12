from django.contrib import admin

from properties.models import PropertyType, PropertyStatus, Property, PropertyImage, PropertyUnit, PropertyUnitImage


# Register your models here.


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon_name')


@admin.register(PropertyStatus)
class PropertyStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status_code')


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage


class PropertyUnitImageInline(admin.TabularInline):
    model = PropertyUnitImage


class PropertyUnitInline(admin.TabularInline):
    model = PropertyUnit


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zipcode', 'created_at', 'update_at')
    inlines = [PropertyUnitInline, PropertyImageInline]


@admin.register(PropertyUnit)
class PropertyUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'price', 'created_at', 'update_at')
    inlines = [PropertyUnitImageInline]
