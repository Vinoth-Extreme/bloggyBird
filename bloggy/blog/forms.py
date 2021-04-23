from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.views import generic
from .models import Post, Category, Comments

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'header_image', 'snippet', 'author', 'body')
        choicesCat = Category.objects.all().values_list('name', 'name')
        title = {
            'class': 'form-control',
            'placeholder': 'Title...',
            'style': 'background-color:black;'
                     'color:white;'
        }
        title_tag = {
            'class': 'form-control',
            'placeholder': 'Title tag...',
            'style': 'background-color:black;'
                     'color:white;'
        }
        author = {
            'class': 'form-control',
            'id': 'author',
            'type': 'hidden',
            'style': 'background-color:black;'
                     'color:white;'
        }
        category = {
            'class': 'form-control',
            'style': 'background-color:black;'
                     'color:white;'
        }
        snippet = {
            'class': 'form-control',
            'style': 'background-color:black;'
                     'color:white;'
        }
        body = {
            'class': 'form-control',
            'placeholder': 'Add content here...',
            'style': 'background-color:black;'
                     'color:white;'
        }

        widgets = {
            'title': forms.TextInput(attrs=title),
            'title_tag': forms.TextInput(attrs=title_tag),
            'author': forms.TextInput(attrs=author),
            'snippet': forms.TextInput(attrs=snippet),
            'category': forms.Select(choices=choicesCat),
            'body': forms.Textarea(attrs=body)
        }



class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')
        formControl = {
            'class': 'form-control',
        }
        widgets = {
            'title': forms.TextInput(attrs=formControl),
            'title_tag': forms.TextInput(attrs=formControl),
            'body': forms.Textarea(attrs=formControl),
            'snippet': forms.TextInput(attrs=formControl)
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)
        done_by = {
            'class': 'form-control',
            'id': 'done_by',
            'type': 'hidden',
        }

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }