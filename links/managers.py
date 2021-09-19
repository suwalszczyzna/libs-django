from django.db import models


class PublishedManager(models.Manager):
    def published(self, **kwargs):
        return self.filter(published=True, **kwargs)
