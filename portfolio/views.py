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
    return render(request, 'portfolio/home.html')


def projects_page_view(request):
    return render(request, 'portfolio/projects.html')


def blog_view(request):
    return render(request, 'portfolio/blog.html')
