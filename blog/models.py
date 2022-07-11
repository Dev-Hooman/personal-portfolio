from django.db import models

# 1) Create your models.  (sketch)
# > title
# > Publication date -> pub_date
# > blog_post_text -> body
# > image
# more features will be added later

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255 )
    category = models.CharField(max_length=100)
    pub_date = models.DateTimeField(blank=True)
    content = models.TextField()
    slug = models.CharField(max_length=130)
    author = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'images/')


    def __str__(self) :
        return f"{self.title} by {self.author}"




# 2) Add the Blog app to the settings


# 3) Create a migration


# 4) Migrate


# 5) Add to the admin