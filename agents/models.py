from django.db import models

from core.models_x import PublishableModel


# Create your models here.


class Agent(PublishableModel):
    """
    Any Object occupying or occupied a property unit on rent
    """
    person = models.ForeignKey('stakeholders.Person', related_name='agents', on_delete=models.CASCADE, null=True,
                               blank=True)
    agency = models.ForeignKey('agencies.Agency', related_name='agents', on_delete=models.CASCADE, null=True,
                               blank=True)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    address = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.person}"
