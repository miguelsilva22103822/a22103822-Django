#  hello/views.py

from django.shortcuts import render


def home_page_view(request):
    return render(request, 'portfolio/home.html')


from django.shortcuts import render

# Create your views here.
