from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from taggit.managers import TaggableManager
from properties.utils import property_images, property_unit_images


# Jeff single-family home (Single unit)
# Ous Apartments (Multi-Unit)
# Josee White lands (Single unit)
#


class PropertyImageBase(models.Model):
    is_primary = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PropertyType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    icon_name = models.CharField(max_length=50)

    @property
    def properties(self):
        props = PropertyUnit.objects.filter(type__name__in=[self.name])
        return props

    def __str__(self):
        return self.name


class PropertyStatus(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    status_code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Property statuses'
        verbose_name = 'Property Status'
        ordering = ('-name',)


class Property(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    # type = models.ForeignKey("properties.PropertyType", on_delete=models.CASCADE, related_name='properties')
    # type = models.CharField(max_length=255)
    # status = models.ForeignKey("properties.PropertyStatus", on_delete=models.CASCADE, related_name='properties')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    size = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def primary_image(self):
        images = self.images.filter(is_primary=True)
        return images[0] if images.exists() else None

    def __str__(self):
        return self.name if self.name else f"Property({self.id})"

    class Meta:
        verbose_name_plural = 'Properties'
        verbose_name = 'Property'
        ordering = ('-created_at',)


class PropertyImage(PropertyImageBase):
    image = models.ImageField(null=False, blank=False, upload_to=property_images)
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.property.name} image"


@receiver(pre_save, sender=PropertyImage)
def ensure_single_primary_image(sender, instance, **kwargs):
    if instance.is_primary:
        # When a new image is marked as primary, un-mark all other images for the same property.
        PropertyImage.objects.filter(property=instance.property).exclude(pk=instance.pk).update(is_primary=False)


class PropertyUnit(models.Model):
    property = models.ForeignKey("properties.Property", on_delete=models.CASCADE, related_name='units')
    name = models.CharField(max_length=50)
    status = models.ForeignKey("properties.PropertyStatus", on_delete=models.CASCADE, related_name='units')
    type = TaggableManager(verbose_name='Type Tags')
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    description = models.TextField(null=True, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # @property
    def full_name(self):
        return f"{self.name}, {self.property.address} {self.property.state}, {self.property.city}"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created_at',)


class PropertyUnitImage(PropertyImageBase):
    image = models.ImageField(null=False, blank=False, upload_to=property_unit_images)
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f"{self.unit.name} image"


@receiver(pre_save, sender=PropertyUnitImage)
def ensure_single_primary_image(sender, instance, **kwargs):
    if instance.is_primary:
        # When a new image is marked as primary, unmark all other images for the same unit.
        PropertyUnitImage.objects.filter(unit=instance.unit).exclude(pk=instance.pk).update(is_primary=False)


class PropertyUnitAmenity(models.Model):
    unit = models.ForeignKey("properties.PropertyUnit", on_delete=models.CASCADE, related_name='amenities')
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    icon_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Property UnitAmenities'
        verbose_name = 'PropertyUnitAmenity'
        ordering = ('-created_at',)
