from django.shortcuts import render
from .models import Blog


# Create your views here.
def showblog(request):
    posts = Blog.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts},)
