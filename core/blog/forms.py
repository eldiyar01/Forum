from django import forms
from django.forms import ModelForm

from .models import News, Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )



























# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['title', 'description', 'body', 'categories', 'author']
#
#         widgets = {
#             'title': forms.TextInput(attrs= {'class': 'form-control'}),
#             'description': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.Textarea(attrs={'class': 'form-control'}),
#             'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
#             'author': forms.Select(attrs={'class': 'form-control'})
#         }