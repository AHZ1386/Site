import re
from django import forms
from .models import User,UserAddress,Otp
from django.contrib.auth.forms import UserCreationForm
class UserCreateForm(UserCreationForm):
    phone_number = forms.IntegerField()

    class Meta:
        model = User
        fields = ['phone_number', 'password1', 'password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name','last_name',]
        
        

class UserAddressForm(forms.ModelForm):
    class Meta:
        model = UserAddress
        fields = ['post_code', 'address', 'provinec', 'house_number']
        
        
class OtpForm(forms.ModelForm):
    class Meta:
        model = Otp
        fields = ['otp']



class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='پسورد قبلی', widget=forms.PasswordInput)
    new_password = forms.CharField(label='پسورد جدید', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Cتایید پسورد جدید', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password != confirm_password:
            raise forms.ValidationError("پسورد های جدید یکی نیستند")


class LoginForm(forms.Form):
    phone_number = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput())
    
