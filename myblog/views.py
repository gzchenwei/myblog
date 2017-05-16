from article.models import Article
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.shortcuts import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout

post_list = Article.objects.all()[::-1]

def about(request):
    return  render(request,'about.html',{'post_list': post_list})

def index(request):
    if request.method == 'POST':
        username = request.POST.get('user_id')
        password = request.POST.get('pwd')
        t = authenticate(username=username, password=password)
        if t is not None:
            login(request, t)
            response = HttpResponseRedirect('/blog/?next=%s' % request.path)
            return response
        else:
            errors="pls check your user and password"
            return render_to_response('index.html',{'errors': errors})
    else:
        return render(request,'index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def test(request):
    return  render(request,'test.html')
