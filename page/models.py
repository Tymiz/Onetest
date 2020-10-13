from django.db import models

class Image(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to='media')
