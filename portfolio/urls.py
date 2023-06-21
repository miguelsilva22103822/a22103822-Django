from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('contacts', views.contacts, name='contacts'),
    path('add_posts', views.add_post, name='add_post'),
    path('post/<str:post_id>/delete', views.delete_post, name='delete_post'),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
