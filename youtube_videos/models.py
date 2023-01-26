from django.db import models


class Video(models.Model):

    title = models.CharField(max_length=2000, null=False, blank=False)
    description = models.CharField(max_length=2000, null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=False)
    thumbnails_url = models.CharField(max_length=2000, null=False, blank=False)