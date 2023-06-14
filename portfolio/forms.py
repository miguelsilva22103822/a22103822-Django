from django.forms import ModelForm
from .models import *

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'area']

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        fields = '__all__'
