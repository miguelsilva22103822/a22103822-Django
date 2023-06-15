from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('projects', views.projects_page_view, name='projects'),
    path('blog', views.blog_view, name='blog'),
]