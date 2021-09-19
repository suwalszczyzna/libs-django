from django.db import models
from core.models import NanoIdModel, TimeStampModel


class Tag(NanoIdModel):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Link(NanoIdModel, TimeStampModel):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=255)
    faviconUrl = models.CharField(max_length=255, null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
