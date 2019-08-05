from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')


# Form example with form.Form (e.g. create form without ModelForm.
# class NameForm(forms.Form):
# your_name = forms.CharField(label='Your name', max_length=100)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)