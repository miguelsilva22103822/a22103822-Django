from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.urls import reverse

from .models import *
from .forms import *


def index_view(request):
    return render(request, 'portfolio/home.html')


def blog_view(request):
    blog_posts = {'posts': Post.objects.all()}
    return render(request, 'portfolio/blog.html', blog_posts)


def contacts_view(request):
    contacts = {'contacts': Contact.objects.all()}
    return render(request, 'portfolio/contacts.html', contacts)
