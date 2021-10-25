from django import forms
from django.db.models import fields
from .models import Employee


class CreateNewList(forms.ModelForm):
    class Meta:
        model =Employee
        fields = ['Name' , 'salary']
