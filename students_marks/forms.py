from django.forms.widgets import NumberInput
from .models import marks
from django import forms

class marks_form(forms.Form):
    name = forms.CharField(
        label="Name of the student",
        max_length=50,
        widget=forms.TextInput(attrs = {'class':'form-control', 'required':True, 'placeholder':'Example: Alex'})
    )

    roll_number = forms.IntegerField(
        label="Student Roll Number",
        widget=forms.NumberInput(attrs={'class':'form-control', 'required':True, 'placeholder':'Example: 12345'})
    )

    maths_marks = forms.FloatField(
        label="Marks in Mathematics",
        widget= forms.NumberInput(attrs = {'class':" form-control",'step':0.1, 'required':True, 'placeholder':'Example: 75.25' })
    )

    physics_marks = forms.FloatField(
        label="Marks in Physics",
        widget=forms.NumberInput(attrs={'class':" form-control",'step':0.1, 'required':True, 'placeholder':'Example: 75.25'})
    )

    chemistry_marks = forms.FloatField(
        label="Marks in Chemistry",
        widget=forms.NumberInput(attrs={'class':" form-control",'step':0.1, 'required':True, 'placeholder':'Example: 75.25'})
    )

    def clean_roll_number(self):
        data = self.cleaned_data.get("roll_number")

        if len(str(data)) != 5:
            raise forms.ValidationError("Please Enter a valid Roll Number (5 digit number)")

        return data

    def clean_maths_marks(self):
        data = self.cleaned_data.get("maths_marks")

        if data < 0  or data > 100:
            raise forms.ValidationError("Marks should be in the range 0 - 100")

        return data

    def clean_physics_marks(self):
        data = self.cleaned_data.get("physics_marks")

        if data < 0  or data > 100:
            raise forms.ValidationError("Marks should be in the range 0 - 100")

        return data

    def clean_chemistry_marks(self):
        data = self.cleaned_data.get("chemistry_marks")

        if data < 0  or data > 100:
            raise forms.ValidationError("Marks should be in the range 0 - 100")

        return data