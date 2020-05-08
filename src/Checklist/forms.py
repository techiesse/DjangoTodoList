from django import forms

from .models import *

#class ChecklistForm(forms.Form):
#    name = forms.CharField(max_length = 50)


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = ['name']
        labels = {
            'name': 'Nome'
        }

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['checked', 'name', 'description']
