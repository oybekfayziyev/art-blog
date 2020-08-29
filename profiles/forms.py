from django import forms
from profiles.models import Profile

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name','bio', 'profile_pic']