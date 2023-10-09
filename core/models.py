from django.db import models


# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    privileges = models.ManyToManyField('core.Privilege', related_name='privileges')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Privilege(models.Model):
    privilege_code = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
