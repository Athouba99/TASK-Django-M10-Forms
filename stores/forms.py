from dataclasses import fields
from django import forms
from .models import StoreItem   


class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem # the model name should be the same name as the imported model
        fields = ["name", "description", "price"] #field will show to the user

