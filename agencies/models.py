from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager

from agencies.utils import agent_images


# Create your models here.


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
