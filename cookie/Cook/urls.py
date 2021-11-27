from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:category_id>/', views.show_post),
    path('create/', views.create),
]
