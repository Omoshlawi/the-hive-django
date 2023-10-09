from django.db import models


# Create your models here.


class PropertyOwner(models.Model):
    """
    Any Object owning a property, can be a system user or can be added by another user
    """
    user = models.ForeignKey('auth.User', related_name='property_owners', on_delete=models.CASCADE, null=True,
                             blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PropertyStaff(models.Model):
    """
    Any object with ability to manage property, either add, update, delete, e.t.c
    """
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='staffs')
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='staffs')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'property')


class Tenant(models.Model):
    """
    Any Object occupying or occupied a property unit on rent
    """
    user = models.ForeignKey('auth.User', related_name='tenants', on_delete=models.CASCADE, null=True, blank=True)
    unit = models.ForeignKey('properties.PropertyUnit', related_name='tenants', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PropertyStaffRole(models.Model):
    staff = models.ForeignKey('stakeholders.PropertyStaff', on_delete=models.CASCADE, related_name='staff_roles')
    role = models.ForeignKey("core.Role", on_delete=models.CASCADE, related_name='staff')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('staff', 'role')
