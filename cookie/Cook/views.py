from django.shortcuts import render, redirect
from .models import Category, Recipe
from .forms import RecipeForm


def show_post(request, category_id):
    if category_id == 2:
        recipe = Recipe.objects.all()
    elif category_id == 8:
        recipe = Recipe.objects.filter(category_id=8)
    elif category_id == 7:
        recipe = Recipe.objects.filter(category_id=7)
    elif category_id == 9:
        recipe = Recipe.objects.filter(category_id=9)
    elif category_id == 6:
        recipe = Recipe.objects.filter(category_id=6)
    elif category_id == 10:
        recipe = Recipe.objects.filter(category_id=10)
    elif category_id == 11:
        recipe = Recipe.objects.filter(category_id=11)
    return render(request, 'Cook/food.html', {'recipe': recipe})


def index(request):
    category = Category.objects.all()
    return render(request, 'Cook/index.html', {'title': 'Главная страница сайта', 'category': category})


def register(request):
    return render(request, 'registration/login.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                form.image = request.FILES['image']
            form.save(commit=True)
            return redirect('/')
        else:
            error = 'Форма была неверной'
    form = RecipeForm()
    context = {'form': form,
               'error': error}
    return render(request, 'Cook/create.html', context)
