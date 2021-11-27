from .models import Recipe
from django.forms import ModelForm, TextInput, NumberInput, Textarea


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'ingredients', 'directions']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите название"
        }),
            'cook_time': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Укажите время приготовления"
            }),
            'ingredients': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите ингредиенты"
            }),
            'directions': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Введите описание"
            }),
        }