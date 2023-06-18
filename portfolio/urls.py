from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index_view, name='home'),
    path('blog', views.blog_view, name='blog'),
    path('contacts', views.contacts_view, name='contacts'),
]