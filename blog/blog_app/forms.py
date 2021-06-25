from .models import Blog
from django import forms


class Blogforms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'desc', 'img']
