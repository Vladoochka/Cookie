from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Category
from .forms import RecipeForm


def show_post(request, category_id):
    return HttpResponse(f"Отображение статьи с id = {category_id}")


def index(request):
    category = Category.objects.all()
    return render(request, 'Cook/index.html', {'title': 'Главная страница сайта', 'category': category})


def create(request):
    error = ''
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма была неверной'
    form = RecipeForm()
    context = {'form': form,
               'error': error}
    return render(request, 'Cook/create.html', context)

