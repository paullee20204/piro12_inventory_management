from django import forms
from .models import Mate

class ItemForm(forms.ModelForm):
    class Meta:
        model = Mate
        fields = '__all__'