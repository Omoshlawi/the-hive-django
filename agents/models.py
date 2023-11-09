from django.db import models

from core.models_x import PublishableModel


# Create your models here.


class Agent(PublishableModel):
    """
    Any Object occupying or occupied a property unit on rent
    """
    user = models.ForeignKey('auth.User', related_name='agents', on_delete=models.CASCADE, null=True, blank=True)
    agency = models.ForeignKey('agencies.Agency', related_name='agents', on_delete=models.CASCADE, null=True,
                               blank=True)
