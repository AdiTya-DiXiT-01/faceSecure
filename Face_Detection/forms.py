from django import forms
from .models import *


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'face_id',
            'name',
            'job',
            'phone',
            'email',
            'bio',
            'image'
        ]
