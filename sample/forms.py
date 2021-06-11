from django import forms
from .models import Employees


class MyForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = "__all__"
