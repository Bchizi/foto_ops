from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.


class photosTestClass(TestCase):
    # set up method
    def setUp(self):
        self.new_category = Category(category_name='Nature')
        self.new_category.save_category()
        self.new_location = Location(location_name='Africa')
        self.new_location.save_location()
        self.new_image = Image(id=1,image_name='lion',image_description='roar!',image_path='media/photo/wallhaven-5wr3m7.jpg',image_category=self.new_category,image_location=self.new_location)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        self.assertTrue(isinstance(self.new_location,Location))
        self.assertTrue(isinstance(self.new_category,Category))
    
    def test_save_method(self):
        self.new_image.save_image()
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects)>0)

    def test_delete_method(self):
        self.new_image.save_image()
        filtered_object = Image.objects.filter(image_name='lion')
        Image.delete_image(filtered_object)
        all_objects = Image.objects.all()
        self.assertTrue(len(all_objects) == 0)

    def test_update_single_object_property(self):
        self.new_image.save_image()
        filtered_object =Image.update_image('Happiness','lion')
        fetched = Image.objects.get(image_name='lion')
        self.assertEqual(fetched.image_name,'lion')
    
    def test_get_image_by_id(self):
        self.new_image.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    def test_search_by_category(self):
        self.new_image.save_image()
        fetch_specific = Category.objects.get(category_name='Happiness')
        self.assertTrue(fetch_specific.category_name=='Happiness')
    
    def test_filter_by_location(self):
        self.new_image.save_image()
        fetch_specific = Location.objects.get(location_name='Mombasa')
        self.assertTrue(fetch_specific.location_name=='Mombasa')