from django.db import models
from psycopg2 import Timestamp


class contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=150)
    content = models.TextField()
    Timestamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return f'Message From {self.name} To devHooman'
        