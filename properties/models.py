from django.db import models

from properties.utils import property_images, property_unit_images


# Create your models here.
class PropertyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    icon_name = models.CharField(max_length=50)


class PropertyStatus(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    status_code = models.CharField(max_length=20, unique=True)


class Property(models.Model):
    name = models.CharField(max_length=50)
    type = models.ForeignKey("properties.PropertyType", on_delete=models.CASCADE, related_name='properties')
    status = models.ForeignKey("properties.PropertyStatus", on_delete=models.CASCADE, related_name='properties')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PropertyImage(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=False, blank=False, upload_to=property_images)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PropertyUnit(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=50)
    status = models.ForeignKey("properties.PropertyStatus", on_delete=models.CASCADE, related_name='units')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PropertyUnitImage(models.Model):
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=False, blank=False, upload_to=property_unit_images)
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PropertyUnitAmenity(models.Model):
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    icon_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
