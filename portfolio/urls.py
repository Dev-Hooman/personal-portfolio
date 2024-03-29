from django.contrib import admin
from django.urls import path, include

#----------------------------------------------------------
#these imports are for MEDIA ROOT
from django.conf import settings
from django.conf.urls.static import static
#----------------------------------------------------------


admin.site.site_header = "AbdulRehman Sarfaraz ADMIN"
admin.site.site_title = "AbdulRehman Sarfaraz ADMIN Portal"
admin.site.index_title = "Welcome to devHooman Portal"


urlpatterns = [
    path('',include("home.urls")),
    path('admin/', admin.site.urls),
    path('blog/',include("blog.urls")),
    path('accounts/', include("allauth.urls")),
    path('user/', include("users.urls") ),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#above addition of static will helps to set root path of media files
#so that we can get images or any sort of media from there.

