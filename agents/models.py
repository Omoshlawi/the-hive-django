from django.db import models


# Create your models here.


class Agent(models.Model):
    """
    Any Object occupying or occupied a property unit on rent
    """
    user = models.ForeignKey('auth.User', related_name='agents', on_delete=models.CASCADE, null=True, blank=True)
    agency = models.ForeignKey('agencies.Agency', related_name='agents', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
