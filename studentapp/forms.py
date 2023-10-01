from django import forms

from studentapp.models import Students


class Studentsform(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'