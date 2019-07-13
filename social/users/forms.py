from django import forms
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
   # first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
   # last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_paswword = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   # birth_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'value': datetime.date.today()}))


    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Password must match")
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__icontains=username).exists():
            raise forms.ValidationError("This username is taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__icontains=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_birth_date(self):
        if datetime.date.today() < self.cleaned_data['birth_date']:
            raise forms.ValidationError("Please Enter A Valid Date")
        return self.cleaned_data['birth_date']

