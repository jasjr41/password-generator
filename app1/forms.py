from django import forms

from app1.models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields=['length', 'uppercase', 'digits', 'special']
        widgets = {
            "length": forms.NumberInput(attrs={"class": "form-control",
                                             "min":8,
                                             "max":32}),
            'uppercase': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'digits': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'special': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'uppercase': 'Include Uppercase Letters',
            'digits': 'Include Numbers',
            'special': 'Include Special Characters',
        }