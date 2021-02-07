from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Password*', required=True, max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm password*', required=True, max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    # To access on admin site (add new user) comment the followintg def
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'invalid': 'Invalid Username', 'required': 'Username is mandatory'}
        self.fields['first_name'].error_messages = {'invalid': 'Invalid First Name', 'required': 'First name is mandatory'}
        self.fields['last_name'].error_messages = {'invalid': 'Invalid Last Name', 'required': 'Last Name is mandatory'}
        self.fields['password1'].error_messages = {'required': 'Password is mandatory'}
        self.fields['password2'].error_messages = {'required': 'Confirm Password is mandatory'}

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'The Username "%s" is already used.' % username)
        return username

    def clean_password2(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        # This method will set the `cleaned_data` attribute
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('The two passwords don\'t match.')
        return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name')

    def clean_password(self):
        return ""
