from django.urls import path

from . import views
urlpatterns = [

    path("", views.blog, name="blog"),
    path('<str:slug>', views.blogPost, name="blogPost"),

]



# MY NOTES
'''
WHAT IS <str:slug> ?
    A "slug" is a way of generating a valid URL, generally using data already obtained. 
    For instance, a slug uses the title of an article to generate a URL. 
    I advise to generate the slug by means of a function, 
    given the title (or another piece of data), rather than setting it manually.
Definition Source: 
    https://stackoverflow.com/questions/427102/what-is-a-slug-in-django
'''