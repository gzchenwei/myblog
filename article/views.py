from django.shortcuts import *

# Create your views here.

from article.models import Article
from django.http import HttpResponse
from datetime import datetime
post_list = Article.objects.all()[::-1][0:10]

def showall(request):
#    post_list = Article.objects.all()[::-1]
    return render(request, 'home.html', {'post_list' : post_list})

def archives(request, arch):
    try:
        arch_list = Article.objects.filter(category=str(arch))[::-1]
    except Article.DoesNotExist:
	raise Http404
    return render(request, 'archives.html', {'arch_list' : arch_list,
                                            'post_list': post_list,
					     'error' : False})
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
#        post_list = Article.objects.all()[::-1]
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post,'post_list': post_list})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

