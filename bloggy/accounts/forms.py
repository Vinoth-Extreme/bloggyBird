from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.forms import forms
from django.contrib.auth.models import User
from django.views import generic
from blog.models import Profile

class SignupForm(UserCreationForm):
    firstname = {
        'class': 'form-control',
        'style': 'background-color:black;'
                 'color:#fff;',
        'placeholder': 'first name...'
    }
    lastname = {
        'class': 'form-control',
        'style': 'background-color:black;'
                 'color:#fff;',
        'placeholder': 'last name...'
    }
    email = {
        'class': 'form-control',
        'style': 'background-color:black;'
                 'color:#fff;',
        'placeholder': 'Email...'
    }
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=firstname))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs=lastname))
    email = forms.EmailField(widget=forms.EmailInput(attrs=email))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username...'
        self.fields['username'].widget.attrs['style'] = 'background-color:black;color:#fff;'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'New Password...'
        self.fields['password1'].widget.attrs['style'] = 'background-color:black;color:#fff;'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password...'
        self.fields['password2'].widget.attrs['style'] = 'background-color:black;color:#fff;'



class UserEditForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', }))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', }))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control', }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url', 'linkedin_url', 'bio')
        formControl = {
            'class': 'form-control',
            'style': 'background-color:black;color:#fff;',
        }
        widgets = {
            'website_url': forms.TextInput(attrs=formControl),
            'facebook_url': forms.TextInput(attrs=formControl),
            'twitter_url': forms.TextInput(attrs=formControl),
            'instagram_url': forms.TextInput(attrs=formControl),
            'linkedin_url': forms.TextInput(attrs=formControl),
            'bio': forms.Textarea(attrs=formControl),
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
