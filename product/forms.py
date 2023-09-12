from dataclasses import fields
from django import forms
from .models import Cart




class Cart_Form(forms.ModelForm):
    class Meta:
        model=Cart
        fields=['product','buy_from_avalable','avalable']