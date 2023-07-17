from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts'),
    path('add_posts', views.add_post, name='add_post'),
    path('post/<str:post_id>/delete', views.delete_post, name='delete_post'),
    path('post/<str:post_id>/like_post', views.like_post, name='like_post'),
    path('post/<str:post_id>/add_comment', views.add_comment, name='add_comment'),
    path('comment/<str:comment_id>/like_comment', views.like_comment, name='like_comment'),
    path('course_subjects', views.course_subjects, name='course_subjects'),
    path('about_me', views.about_me, name='about_me'),
    path('projects', views.projects, name='projects'),
    path('login_view', views.login_view, name='login'),
    path('logout_view', views.logout_view, name='logout_view'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
