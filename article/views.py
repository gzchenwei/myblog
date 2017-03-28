from django.shortcuts import *

# Create your views here.

from article.models import Article
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def require_login(view):
    def new_view(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return view(request, *args, **kwargs)
    return new_view

def showall(request):
    posts = Article.objects.all()[::-1]
    paginator  = Paginator(posts ,3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list' : post_list,
                                       'posts': posts})

def archives(request, arch):
    post_list = Article.objects.all()[::-1][0:10]
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
        post_list = Article.objects.all()[::-1]
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post' : post,'post_list': post_list})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

