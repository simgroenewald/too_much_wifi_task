
from django.conf.urls import url
from . import views

app_name= 'images'

urlpatterns = [
    url(r'^$', views.image_list, name = 'image_list'),
    # Urls have to be before the image_slug url
    # If it is after it could take in the url as the image_slug
    # \w means any letter or number includes hyphen and plus for any length
    url(r'^(?P<image_name>[\w-]+)/$', views.colour_finder, name = 'colour_finder'),
]
