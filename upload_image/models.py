from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Image(models.Model):
    image_name = models.CharField(max_length = 100)
    image_file = models.ImageField(upload_to='media/',width_field = 'image_width', height_field='image_height')
    image_width = models.IntegerField(default=0)
    image_height = models.IntegerField(default=0)
    # create this later thumbnail =
    image_date = models.DateTimeField(auto_now_add = True)
    # Associates image with user who has uploaded it
    # App does not have delete functionality so for now the on_delete is do nothing
    image_user = models.ForeignKey(User, default=None,on_delete = models.DO_NOTHING)

    # the __str__ function ensures that a generic object isn't returned
    # imagefile represets the pathway to the image
    def __str__(self):
        return self.image_name
        #+ ": " + str(self.imagefile)
