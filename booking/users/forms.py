# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Κωδικός πρόσβασης*', required=True, max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Κωδικός πρόσβασης'}))
    password2 = forms.CharField(label='Επιβεβαίωση κωδικού πρόσβασης*', required=True, max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Επιβεβαίωση κωδικού πρόσβασης'}))

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    # To access on admin site (add new user) comment the followintg def
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'invalid': 'Μη έγκυρο "Όνομα χρήστη"', 'required': 'Υποχρεωτικό πεδίο "Όνομα χρήστη"'}
        self.fields['email'].error_messages = {'required': 'Υποχρεωτικό πεδίο "Ηλ. ταχυδρομείο"', 'invalid':'Μη έγκυρη μορφή "Ηλ. ταχυδρομείου". Σωστή μορφή: name@email.com'}
        self.fields['first_name'].error_messages = {'invalid': 'Μη έγκυρο "Όνομα"', 'required': 'Υποχρεωτικό πεδίο "Όνομα"'}
        self.fields['last_name'].error_messages = {'invalid': 'Μη έγκυρο "Επώνυμο"', 'required': 'Υποχρεωτικό πεδίο "Επώνυμο"'}
        self.fields['password1'].error_messages = {'required': 'Υποχρεωτικό πεδίο "Κωδικός πρόσβασης"'}
        self.fields['password2'].error_messages = {'required': 'Υποχρεωτικό πεδίο "Επιβεβαίωση κωδικού πρόσβασης"'}

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Το όνομα χρήστη "%s" ήδη χρησιμοποιείται.' % username)
        return username

    def clean_password2(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        # This method will set the `cleaned_data` attribute
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Τα δύο πεδία, σχετικά με τον κωδικό πρόσβασης, δεν ταιριάζουν')
        return password2


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def clean_password(self):
        return ""


class ChangePasswordForm(UserChangeForm):
    new_password = forms.CharField(label='Νέος κωδικός πρόσβασης', required=True, max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Νέος κωδικός πρόσβασης'}))

    class Meta:
        model = CustomUser
        fields = ['new_password',]

    def clean_password(self):
        return ""
