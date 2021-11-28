from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('<int:category_id>/', views.show_post),
    url('create/', views.create),
]
