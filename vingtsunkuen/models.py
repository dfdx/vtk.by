
from django.db import models
from datetime import datetime


class PhotoCategory(models.Model):
    name = models.CharField(max_length=256, default="")
    subpath = models.CharField(max_length=256, default="")
    order = models.IntegerField()

    def __str__(self):
        return "PhotoCategory(%s)" % (self.name,)

    
class PhotoAlbum(models.Model):
    name = models.CharField(max_length=256, default="")
    subpath = models.CharField(max_length=256, default="")
    order = models.IntegerField()
    category = models.ForeignKey('PhotoCategory', on_delete=models.CASCADE)

    def __str__(self):
        return ("PhotoAlbum(%s: %s)" % (self.category.name, self.name))
