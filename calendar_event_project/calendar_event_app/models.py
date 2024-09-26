from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Events(models.Model): 
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    image_url = models.URLField()
    registration_link = models.URLField()
    short_description = models.CharField()
    long_description = models.CharField()
    tags = models.ManyToManyField(Tag, related_name='events')