from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

from django.db.models import Count

from blog.models import Blog
import string

def blog(request):

    allPost = Blog.objects.all()

    context = {
        'allPost':allPost,
    }

    return render(request, 'blog/blog.html',context)


def blogPost(request, slug):
    blogPost = Blog.objects.filter(slug=slug).first()
    context = {'blogPost' : blogPost}
    return render(request, 'blog/blogPost.html', context)

