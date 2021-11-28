from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

# class Tag(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Название')
#     slug = models.SlugField(max_length=100)
#
#     class Meta:
#         verbose_name_plural = 'Теги'
#         verbose_name = 'Тег'


# class Post(models.Model):
#     author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='articles/')
#     text = models.TextField()
#     category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
#     tags = models.ManyToManyField(Tag, related_name='post')
#     create_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name_plural = 'Посты'
#         verbose_name = 'Пост'


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cook_time = models.CharField(max_length=100)
    ingredients = models.TextField()
    directions = models.TextField()
    category = models.ForeignKey(Category, related_name='recipe', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='articles/')
    # post = models.ForeignKey(Post, related_name='recipe', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Рецепты'
        verbose_name = 'Рецепт'

    def __str__(self):
        return self.name


# class Comment(models.Model):
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=100)
#     website = models.CharField(max_length=150)
#     message = models.TextField(max_length=500)
#     post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = 'Комментарии'
#         verbose_name = 'Комментарий'
