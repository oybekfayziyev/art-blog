from django import forms
from .models import Post

class PostForm(forms.Form):
    user = forms.CharField(max_length=350, required=False)
    image = forms.ImageField(required=False)
   
    description = forms.CharField(widget = forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : "What's in your mind?",
    }))

