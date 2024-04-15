from django import forms
from .models import *

class QoidaForm(forms.ModelForm):
    class Meta:
        model = YHQQoida
        fields = ['text', 'img']
        widgets = {
            'img': forms.ClearableFileInput(attrs={'multiple': True, 'required': False})
        }
