""" from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100) """

from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model= BlogComment
        fields= ["firstname", "lastname", "email", "comment"]