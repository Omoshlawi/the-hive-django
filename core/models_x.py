from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class PublishableModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    objects = models.Manager()  # The default manager
    published_objects = PublishedManager()  # Custom manager for published objects

    class Meta:
        abstract = True
