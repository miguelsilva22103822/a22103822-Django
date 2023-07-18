import time

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *

from bs4 import BeautifulSoup
import requests
import csv

import datetime


def home(request):
    return render(request, 'portfolio/home.html')


def blog(request):
    context = {
        'posts': Post.objects.all().order_by('-likes'),
        'comments': Comment.objects.all().order_by('-likes'),
        'authenticated': request.user.is_authenticated,
    }
    return render(request, 'portfolio/blog.html', context)


def contacts(request):
    contacts_social = {'contacts': Contact.objects.all()}
    return render(request, 'portfolio/contacts.html', contacts_social)


def about_me(request):
    return render(request, 'portfolio/about_me.html')


def projects(request):
    project_list = {'projects': Project.objects.all()}
    return render(request, 'portfolio/projects.html', project_list)


def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('portfolio:blog')
    else:
        post_form = PostForm()

    return render(request, 'portfolio/add_post.html', {'form': post_form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST' and request.user.is_authenticated:
        post.delete()
        return redirect('portfolio:blog')

    return redirect('portfolio:blog')


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.likes += 1
        post.save()
        return redirect('portfolio:blog')

    return render(request, 'portfolio/blog.html', {'post': post})


def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        comment_text = request.POST.get('comment_text')
        comment = Comment(text=comment_text, post_id=post)
        comment.save()

        return redirect('portfolio:blog')

    return render(request, 'portfolio/blog.html', {'post': post})


def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        comment.likes += 1
        comment.save()
        return redirect('portfolio:blog')

    return render(request, 'portfolio/blog.html', {'comment': comment})


def course_subjects(request):
    context = {
        'years': Year.objects.all(),
        'semesters': Semester.objects.all(),
        'subjects': Subject.objects.all(),
        'persons': Person.objects.all(),
    }

    return render(request, 'portfolio/course_subjects.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return render(request, 'portfolio/login.html', {'message': "You are already logged in."})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('portfolio:home'))
        else:
            return render(request, 'portfolio/login.html', {'message': "Invalid credentials."})

    return render(request, 'portfolio/login.html')


def logout_view(request):
    logout(request)
    return render(request, 'portfolio/login.html', {'message': 'Logged out.'})
