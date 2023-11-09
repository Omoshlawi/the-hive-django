from django.contrib import admin

from properties.models import PropertyType, PropertyStatus, Property, PropertyImage, PropertyUnit, PropertyUnitImage, \
    PropertyAmenity, Amenity


# Register your models here.

@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon_name')
    search_fields = ('name',)


@admin.register(PropertyStatus)
class PropertyStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'status_code')
    search_fields = ('name',)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'icon_name')
    search_fields = ('name',)


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage


class PropertyAmenityInline(admin.TabularInline):
    model = PropertyAmenity
    search_fields = ['amenity__name']
    autocomplete_fields = ['amenity']


class PropertyUnitImageInline(admin.TabularInline):
    model = PropertyUnitImage


class PropertyUnitInline(admin.TabularInline):
    model = PropertyUnit


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'state', 'zipcode', 'created_at', 'update_at')
    search_fields = ('name',)
    inlines = [
        PropertyImageInline,
    ]


@admin.register(PropertyUnit)
class PropertyUnitAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'price', 'published', 'created_at', 'update_at')
    list_editable = ['published']
    search_fields = ('name',)
    autocomplete_fields = ('property', 'type', 'status')
    inlines = [PropertyUnitImageInline, PropertyAmenityInline]
