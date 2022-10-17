
from django import forms
from .models import StoreItem   


class StoreItemForm(forms.Model):
    class Meta:
        model = StoreItem # the model name should be the same name as the imported model
        fileds = ["name", "desscription", "price"]
         


    