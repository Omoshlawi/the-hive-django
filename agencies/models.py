from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.managers import TaggableManager

from agencies.utils import agent_images
from core.models_x import PublishableModel


# Create your models here.


class Agency(PublishableModel):
    """
    Any Object occupying or occupied a property unit on rent
    """
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to=agent_images)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    tags = TaggableManager()

    @property
    def fq_address(self):
        return f"{self.zipcode} {self.state} {self.address}, {self.city}"

    class Meta:
        verbose_name_plural = "Agencies"
