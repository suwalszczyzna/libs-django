from functools import partial
from nanoid import generate
from django.db import models


class NanoIdModel(models.Model):
    id = models.CharField(max_length=15, default=partial(generate, size=10))

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
