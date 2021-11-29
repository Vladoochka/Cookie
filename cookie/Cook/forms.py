from .models import Recipe
from django.forms import ModelForm, TextInput, Textarea


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'ingredients', 'directions', 'category', 'image', 'tags']
        widgets = {'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Введите название"
        }),
            'cook_time': TextInput(attrs={
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
