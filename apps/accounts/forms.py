from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model

from .models import Profile
User = get_user_model()


class LoginForm(forms.Form):
	username = forms.CharField(label="Email")
	password = forms.CharField(widget = forms.PasswordInput)
	

class RegisterForm(UserCreationForm):
    username  = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. yourname0980'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]
        widgets = {
        'email':    forms.EmailInput(attrs={'class':'form-control'}),
        }

    def clean_email(self):
        restricted = ['admin','superuser','staff']
        email = self.cleaned_data.get('email')
        for i in restricted:
            if email.startswith(i):
                raise forms.ValidationError("This email is not allowed")
        return email

    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit = False)
        user.is_active = False
        if commit:
            user.save()
        return user


class UpdateProfileModelForm(forms.ModelForm):
    class Meta:
        model  = Profile 
        fields = ['name','bio','image']