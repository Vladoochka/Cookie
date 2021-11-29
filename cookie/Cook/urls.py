from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:category_id>/', views.show_post),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('accounts.urls')),
    url('create/', views.create),
    path('search/', views.SearchResultsView.as_view(), name='search_results')
]
