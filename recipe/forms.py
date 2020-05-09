from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'cuisine',
            'time_hours',
            'time_min',
            'ingredients',
            'method'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for k, _ in self.fields.items():
            self.fields[k].widget.attrs.update({'class': 'form-control'})
