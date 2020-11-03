from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Blog(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_date = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    blog_text = models.TextField(max_length=1500)
    blog_image = models.ImageField(upload_to='blog_images/')


