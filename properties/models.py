from django.db import models


# Create your models here.
class PropertyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)


class PropertyStatus(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status_code = models.CharField(max_length=255, unique=True)


class Property(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey("properties.PropertyType", on_delete=models.CASCADE, related_name='properties')
    status = models.ForeignKey("properties.PropertyStatus", on_delete=models.CASCADE, related_name='properties')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    address = models.ImageField(null=False, blank=False)
    city = models.ImageField(null=False, blank=False)
    state = models.ImageField(null=False, blank=False)
    zipcode = models.ImageField(null=False, blank=False)


class PropertyImage(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=False, blank=False)


class PropertyUnit(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=255)
    status = models.ForeignKey("properties.PropertyStatus", on_delete=models.CASCADE, related_name='units')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)


class PropertyUnitImage(models.Model):
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(null=False, blank=False)


class PropertyUnitAmenity(models.Model):
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=255)
