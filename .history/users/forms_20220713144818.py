from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import ugettext_lazy as _

from .models import User, TutorProfile, StudentProfile

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")
    password2 = forms.CharField(required=True, help_text='Enter the same password as before, for verification.', widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password Confirmation")
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'password1', 'password2')
        widgets = {
            'name':forms.TextInput(attrs={'autofocus':''}),
        }
        
class CustomUserChangeForm(forms.ModelForm):
                
    phone =  PhoneNumberField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False, region="IN", label="Mobile No.")
    class Meta:
        model = User
        fields = ('avtar', 'name', 'phone', 'address')
        # widgets = {
        #     'avtar': forms.FileInput(attrs={'class':'form-control','id':'avtar-image-upload', 'accept':'.jpg, .png, image/jpeg, image/png'}),
        #     'name': forms.TextInput(attrs={'class':'form-control', 'autofocus':'', 'tabindex':'1'}),
        #     'address': forms.TextInput(attrs={'class':'form-control', 'id':'address', 'tabindex':'3'}),
        # }
        
class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'autofocus':'', 'tabindex':'1'}))
    new_password1 = forms.CharField(label=_("New Password"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'autofocus':'', 'tabindex':'2'}))
    new_password2 = forms.CharField(label=_("New Password Confirmation"),
                                   widget=forms.PasswordInput(attrs={'class':'form-control', 'autofocus':'', 'tabindex':'3'}))
        

class TutorProfileForm(forms.ModelForm):
    intro_video = forms.FileField(widget=forms.FileInput(attrs={'accept':'.mp4, .mkv, .3gp'}), required=False, label="Upload Intro Video")
    class Meta:
        model = TutorProfile
        fields = "__all__"
