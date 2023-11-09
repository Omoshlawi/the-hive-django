from django.contrib import admin

from agencies.models import Agency


# Register your models here.


@admin.register(Agency)
class AgencyAdmin(admin.ModelAdmin):
    list_display = ("name", 'city', 'state', 'zipcode', 'email', 'phone_number',)
