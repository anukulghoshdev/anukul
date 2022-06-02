from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm #UserCreationForm -> username', 'password1', 'password2'
from django.contrib.auth.models import User

from user_auth.models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email Address')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserProfileChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

class UserProfilePic(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
