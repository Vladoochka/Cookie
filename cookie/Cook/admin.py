from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models


class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'create_at']
    inlines = [RecipeInline]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Recipe)
admin.site.register(models.Comment)
