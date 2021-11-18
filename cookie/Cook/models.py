from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey('self', related_name='children', on_delete=models.SET_NULL, null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

