from django.urls import path
from .views import SignUpView
from django.conf.urls import url

urlpatterns = [
    url('signup/', SignUpView.as_view(), name='signup'),
]