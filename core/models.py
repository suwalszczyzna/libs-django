from functools import partial
from nanoid import generate
from django.db import models


def generate_nanoid():
    return generate()


class NanoIdModel(models.Model):
    id = models.CharField(primary_key=True, max_length=30, default=generate_nanoid)

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
