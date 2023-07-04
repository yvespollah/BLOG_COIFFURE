from django import forms
from .models import *

class BlogForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'name',
            'email',
            'body'
        ]
        
     
    
    