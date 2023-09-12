from django import forms 
from .models import User




class SignUpform (forms.ModelForm):
    class Meta:
        model=User
        fields=('password1','password2','country','email','national_Code','phone','address1','address2','gender','age','description')