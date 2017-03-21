from article.models import Article
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import *
post_list = Article.objects.all()[::-1]

def about(request):
    return  render(request,'about.html',{'post_list': post_list})
