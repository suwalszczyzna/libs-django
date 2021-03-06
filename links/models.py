from django.db import models

from core.models import NanoIdModel, TimeStampModel
from .managers import PublishedManager


class Tag(NanoIdModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Link(NanoIdModel, TimeStampModel):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    faviconUrl = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    published = models.BooleanField(default=False)

    objects = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
