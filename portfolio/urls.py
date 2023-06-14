from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('blog', views.blog_view, name='blog'),
    path('jsplayground', views.js_playground_view, name='jsplayground'),
    path('comentarios', views.comentarios_view, name='comentarios'),
    path('newAutor', views.add_author, name='newAuthor'),
    path('newPost', views.add_post, name='newPost'),
    path('newComentario', views.insereComentario, name='newComentario'),
    path('editPost/<int:postId>', views.editPost_view, name='editPost'),
    path('apagaPost/<int:postId>', views.apagaPost_view, name='apagaPost'),
    path('addLike/<int:postId>', views.aumentaLike, name='addLike'),
    path('diminuiLike/<int:postId>', views.diminuiLike, name='diminuiLike'),
    path('login', views.login_view, name='login'),
    path('login_page', views.login_page_view, name='login_page')
]