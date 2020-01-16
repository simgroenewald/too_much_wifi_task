from django.shortcuts import render
from django.views.generic.detail import DetailView
# Imports the model that is needed to view the images
from upload_image.models import User_Image
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import os, sys
from PIL import Image
from pathlib import Path

# user needs to be logged in for it to work
@login_required(login_url="/accounts/login/")
# Defines the image_list function
def image_list(request):
    # Fetches all images and orders them by date posted
    images = User_Image.objects.all().order_by('image_date')
    # The second parameter in {} contains the data that is passed to the template
    # The images variable is sent to the template
    return render(request, 'images/image_list.html', {'images':images})

# user needs to be logged in for it to work
@login_required(login_url="/accounts/login/")
# This defines the get_colour function
def colour_finder(request, image_name):
    # Gets the specific instance of the image selected
    image = User_Image.objects.get(image_name = image_name)
    # Gets the image files path in string format
    im_path_str = image.image_file.path
    # Converts the string path to the path format
    im_path = Path(im_path_str)
    # Opens the image using the path
    im = Image.open(im_path)
    # Converts the image to RGB values
    im = im.convert('RGB')
    # Gets the height of the image
    height = image.image_height
    # Gets the width of the image
    width = image.image_width
    # Calculates the middle pixels y value
    pixel_y = height/2
    # Calculates the middle pixels x value
    pixel_x = width/2
    # Gets the RGB value of the pixel with those x and y coordinates
    RGB = im.getpixel((pixel_x,pixel_y))

    # R,G,B = RGB
    # Returns the specific image selected and the RGB value to the template
    return render(request, 'images/colour_finder.html', {'image':image,'rgb_value': RGB})
