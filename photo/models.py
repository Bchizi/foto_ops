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
    image_path = models.ImageField(upload_to='photo/')
    image_name = models.CharField(max_length=30)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location)   
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
    
    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(image_category__category_name__icontains=search_term)
        return search_result
    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result
    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()

