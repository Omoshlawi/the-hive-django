from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager

from stakeholders.utils import agent_images

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('U', 'Unknown'),
]


# Create your models here.

class Person(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='person', null=True, blank=True)
    surname = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = PhoneNumberField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')
    description = models.TextField(null=True, blank=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class PersonAttribute(models.Model):
    """
    Extra person attributes needed
    """
    person = models.ForeignKey("stakeholders.Person", on_delete=models.CASCADE, related_name='attributes')
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=255)


class PropertyOwner(models.Model):
    """
    Any Object owning a property, can be a system user or can be added by another user
    """
    user = models.ForeignKey('auth.User', related_name='property_owners', on_delete=models.CASCADE, null=True,
                             blank=True)

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
    role = models.ForeignKey("core.Role", on_delete=models.CASCADE, related_name='staff_roles')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('staff', 'role')


class Agency(models.Model):
    """
    Any Object occupying or occupied a property unit on rent
    """
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to=agent_images)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager()


class Agent(models.Model):
    """
    Any Object occupying or occupied a property unit on rent
    """
    user = models.ForeignKey('auth.User', related_name='agents', on_delete=models.CASCADE, null=True, blank=True)
    agency = models.ForeignKey('stakeholders.Agency', related_name='agents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
