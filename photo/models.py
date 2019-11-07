from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
class Image(models.Model):
    image = models.ImageField(upload_to='photo/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)   
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name