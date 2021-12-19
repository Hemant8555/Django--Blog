from django.shortcuts import render
from django.http import HttpResponse
from .models import blogpost
# Create your views here.


def index(request):
    article = blogpost.objects.all()
    return render(request, 'index.html', {'article': article})


def blog(request, id):
    article = blogpost.objects.get(post_id=id)
    return render(request, 'blog.html', {'article': article})
