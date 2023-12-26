from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from apps.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('price', 'image', 'category', 'quantity', 'title')
        # exclude = ('created_at',)


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-type Password'}))

    def clean_password(self):
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('Confirm password is not correct')
        return make_password(password)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'confirm_password')
