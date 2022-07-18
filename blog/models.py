from django.db import models
from users.models import userAccount
from django.utils.timezone import now
from django.db.models.deletion import CASCADE
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

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(userAccount, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog,on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)


# 2) Add the Blog app to the settings


# 3) Create a migration


# 4) Migrate


# 5) Add to the admin