from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name="home" ),
    path("about", views.about, name="about"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contactUs, name="contact"),
    path("search", views.search, name="search"),
]