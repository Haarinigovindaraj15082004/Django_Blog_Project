from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    blog_title = "Latest Posts"
    posts = [
        {'title' : 'Post 1' , 'content' : 'Content of Post 1'},
        {'title' : 'Post 2' , 'content' : 'Content of Post 2'},
        {'title' : 'Post 3' , 'content' : 'Content of Post 3'},
        {'title' : 'Post 4' , 'content' : 'Content of Post 4'},
    ]
    return render(request, 'index.html', {'blog_title' : blog_title, 'posts' : posts})

def detail(request, post_id):
    return render(request, 'detail.html')
def old_url_redirect(request):
    return redirect(reverse('Blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is new url view")