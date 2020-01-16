from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms

# user needs to be logged in for it to work
# first parameter redirects to the login page
@login_required(login_url="/accounts/login/")
# Defines the upload_image function
def upload_image(request):
    # If this is a post request then the following will run
    if request.method == 'POST':
        # request.FILES is needed for uploading files
        form = forms.Upload_Image(request.POST, request.FILES)
        # If the form is valid then the following will run
        if form.is_valid():
            # This saves an instance of the form but does not commit the action
            instance = form.save(commit = False)
            # The image_user is equal to the current user making the request
            instance.image_user = request.user
            # Image instance saves with the image_user added to it
            instance.save()
            # If the upload was successful the user will be redirected to the image list
            return redirect('images:image_list')
    # This will run if it is not a post request and render a blank form
    else:
        form = forms.Upload_Image()
    return render(request, 'upload_image/upload_image.html',{'form':form})
