from django.db import models
from devshortly.utils.base62 import base_encode

# Create your models here.


def generate_slug(url):
    return base_encode(hash(url))


class URL(models.Model):
    url = models.URLField()
    slug = models.SlugField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_slug(url=self.url)
        super(URL, self).save(*args, **kwargs)
