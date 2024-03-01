from django import forms
from admin_page.models import Image
class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('name','image')