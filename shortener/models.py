from django.db import models
from . import url_validator


# Create your models here.
class Url(models.Model):
    link = models.URLField(validators=[url_validator.validate_url])
    uuid = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.uuid
