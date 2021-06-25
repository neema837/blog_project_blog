from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to='image')
    date = models.DateTimeField(auto_now=False)
