from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


# Form example with form.Form (e.g. create form without ModelForm.
# class NameForm(forms.Form):
# your_name = forms.CharField(label='Your name', max_length=100)


# t

class Testform(forms.Form):
    your_fname = forms.CharField(label='Your First name', max_length=25)
    your_lname = forms.CharField(label='Your Last name', max_length=35)