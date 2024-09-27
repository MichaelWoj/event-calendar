from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Events(models.Model): 
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    duration = models.IntegerField()
    location = models.CharField(max_length=255,null=True, blank=True)
    image_url = models.URLField()
    registration_link = models.URLField(null=True, blank=True)
    short_description = models.CharField(max_length=500)
    long_description = models.CharField(null=True, blank=True, max_length=5000)
    tags = models.ManyToManyField(Tag, related_name='events')

    def __str__(self):
        return self.name    