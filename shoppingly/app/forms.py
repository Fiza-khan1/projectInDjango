from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UsernameField,PasswordResetForm
from django.utils.translation import gettext_lazy,gettext as _
from django.contrib.auth.forms import SetPasswordForm
from .models import Customer
class RegForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password1 = forms.CharField(
        max_length=100,
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        max_length=100,
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )
 

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already registered.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords do not match.")
        return password2

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

class loginForm(AuthenticationForm):
    username = UsernameField(label='username', widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label =_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}))
    

class passChange(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}),
        label="Old Password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        label="Confirm New Password"
    )

class passResetForm(PasswordResetForm):
       email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'abcd@gmail.com','class': 'form-control'}),
        label="Email"
    )

class passwordSetting(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=100,
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
    new_password2 = forms.CharField(
        max_length=100,
        widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'})
    )

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = ['name', 'locality', 'city', 'zipcode']
        widgets={
                'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
                'locality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Locality'}),
                'city': forms.Select(attrs={'class': 'form-control'}),
                'zipcode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Zipcode'}),
                'state': forms.Select(attrs={'class': 'form-control'}), 
        }