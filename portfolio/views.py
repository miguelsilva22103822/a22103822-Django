from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def home(request):
    return render(request, 'portfolio/home.html')


def blog(request):
    blog_posts = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', blog_posts)


def contacts(request):
    contacts_social = {'contacts': Contact.objects.all()}
    return render(request, 'portfolio/contacts.html', contacts_social)


def about_me(request):
    return render(request, 'portfolio/about_me.html')


def projects(request):
    return render(request, 'portfolio/projects.html')


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio:blog')
    else:
        form = PostForm()

    return render(request, 'portfolio/add_post.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('portfolio:blog')

    return render(request, 'portfolio/blog.html', {'post': post})


def course_subjects(request):
    context = {
        'years': Year.objects.all(),
        'semesters': Semester.objects.all(),
        'subjects': Subject.objects.all(),
        'persons': Person.objects.all(),
    }

    return render(request, 'portfolio/course_subjects.html', context)
