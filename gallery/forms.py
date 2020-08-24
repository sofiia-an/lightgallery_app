from django import forms
from gallery.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'img_tag', 'picture')