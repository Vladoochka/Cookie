from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Название')
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    cook_time = models.CharField(max_length=100, verbose_name='Время приготовления')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    directions = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(
        Category,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Категория')
    image = models.ImageField(upload_to='articles/', verbose_name='Картинка')
    tags = models.ManyToManyField(Tag, related_name='recipe', verbose_name='Теги')

    class Meta:
        verbose_name_plural = 'Рецепты'
        verbose_name = 'Рецепт'

    def __str__(self):
        return self.name
