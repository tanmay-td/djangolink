from .models import shorturl
from django import forms

class CreateNew(forms.ModelForm):
    class Meta:
        model =shorturl
        fields ={'orignal_url'}

        widgets ={
            'orignal_url': forms.TextInput(attrs={'class': 'form-control'})
        }