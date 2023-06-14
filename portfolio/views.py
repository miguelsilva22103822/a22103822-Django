from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def home_page_view(request):
	context = {
		'projetos': Project.objects.all().order_by('-ano'),
	}

	return render(request, 'portfolio/home.html', context)

def login_page_view(request):
	return render(request, 'portfolio/login.html')

def js_playground_view(request):
	return render(request, 'portfolio/javascript-playground.html')
def blog_view(request):
	context = {
		'autores': Author.objects.all(),
		'posts': Post.objects.all()
	}
	return render(request, 'portfolio/blog.html', context)

def comentarios_view(request):

	context = {
		'postTitle': Post.titulo,
		'comentarios': Comentario.objects.all()
	}

	return render(request, 'portfolio/comentarios.html', context)

def add_author(request):

	form = AuthorForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('portfolio:blog')

	context = {'form': form}

	return render(request, 'portfolio/newAuthor.html', context)

def add_post(request):
	form = PostForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('portfolio:blog')

	context = {'form': form}

	return render(request, 'portfolio/newPost.html', context)

@login_required
def editPost_view(request, postId):
	post_view = get_object_or_404(Post, pk=postId)

	if request.method == 'POST':
		form = PostForm(request.POST, instance=post_view)

		if form.is_valid():
			form.save()
			return redirect('portfolio:blog')
	else:
		form = PostForm(instance=post_view)


	context = {
		'post': Post,
		'postId': postId,
		'form': form
	}

	return render(request, 'portfolio/editPost.html', context)

def apagaPost_view(request, postId):
	Post.objects.get(id= postId).delete()

	return HttpResponseRedirect(reverse('portfolio:blog'))

def insereComentario(request):
	form = ComentarioForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('portfolio:blog')

	context = {'form': form}

	return render(request, 'portfolio/newComentario.html', context)

def aumentaLike(request, postId):

	post = get_object_or_404(Post, pk=postId)
	post.like += 1
	post.save()

	response = HttpResponse("like aumentou")
	response.status_code = 200

	return response

def diminuiLike(request, postId):

	post = get_object_or_404(Post, pk=postId)
	post.like -= 1
	post.save()

	response = HttpResponse("like diminuiu")
	response.status_code = 200

	return response

def login_view(request):
	username = request.POST["username"]
	password = request.POST["password"]

	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
		return redirect('portfolio:blog')
	else:
		return redirect('portfolio:login_page')



