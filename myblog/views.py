from article.models import Article
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import * 

def about(request):
    return  render(request,'about.html')
