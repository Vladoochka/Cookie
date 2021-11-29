from django.shortcuts import render, redirect
from .models import Category, Recipe, Tag
from .forms import RecipeForm
from django.views.generic import ListView
from django.db.models import Q


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


class SearchResultsView(ListView):
    model = Recipe
    template_name = 'Cook/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Recipe.objects.filter(Q(name__icontains=query) | Q(ingredients__icontains=query))
        return object_list
