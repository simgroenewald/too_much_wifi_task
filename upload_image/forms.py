# imports the idea of forms
from django import forms
# imports out models in the current directory
from . import models

class Upload_Image(forms.ModelForm):
    # Define here which fields need to be present
    class Meta:
        # states from which model
        model = models.User_Image
        # states which fields form the model
        fields =['image_name','image_file']
