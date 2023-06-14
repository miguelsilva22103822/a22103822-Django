from django.db import models

# Create your models here.

class BlogOwner(models.Model):
    repo = models.CharField(max_length=600, null=False)
    python_anywhere = models.CharField(max_length=600, null=False)

    def __str__(self):
        return self.repo

class Blog(models.Model):
    nome_Blog = models.CharField(max_length=100, null=False)
    conta = models.OneToOneField(BlogOwner, on_delete=models.CASCADE, related_name="blogOwner")

    def __str__(self):
        return self.nome_Blog

class Area(models.Model):
    nome = models.CharField(max_length=100, null=False)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="areas")

    def __str__(self):
        return  self.nome

class Post (models.Model):
    titulo = models.CharField(max_length=100, null=False)
    conteudo = models.CharField(max_length=1000, null=False)
    like = models.IntegerField(default=0)
    #imagem = models.ImageField()

    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="artigo")
    def __str__(self):
        return self.titulo

class Comentario (models.Model):
    conteudo = models.CharField(max_length=1000, null=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentario")
    def __str__(self):
        return self.conteudo

class Author(models.Model):
    nome = models.CharField(max_length=100, null=False)
    apelido = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=250, null=False)
    verificado = models.BooleanField()

    posts = models.ManyToManyField(Post, related_name="autor")
    areas = models.ManyToManyField(Area, related_name="autor")

    def __str__(self):
        return self.nome + self.apelido

class Project(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    descricao = models.CharField(max_length=100, null=False)
    ano = models.IntegerField(null=False)
    cadeira = models.CharField(max_length=100)
    link_repo = models.CharField(max_length=400, blank=True)
    pessoas = models.CharField(max_length=300)
    def __str__(self):
        return self.titulo

