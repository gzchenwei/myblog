from django.shortcuts import *

# Create your views here.

from article.models import Article
from django.http import HttpResponse
from datetime import datetime

def showall(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list' : post_list})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
	raise Http404
    return render(request, 'archives.html', {'post_list' : post_list,
					     'error' : False})
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post})	

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

