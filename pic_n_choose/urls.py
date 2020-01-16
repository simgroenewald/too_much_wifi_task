
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views

# Needed for media that is uploaded
from django.conf import settings
from django.conf.urls.static import static

# Needed for the static images
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.homepage, name = 'homepage'),
    url(r'^upload-image/',include('upload_image.urls')),
    url(r'^images/', include('images.urls')),
    url(r'^accounts/', include('accounts.urls')),

]

# Needed for the static images
urlpatterns += staticfiles_urlpatterns()
# Needed for the media that is uploaded
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
