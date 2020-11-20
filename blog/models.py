from django.db import models
from datetime import datetime, timedelta


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now()+timedelta(days=30))
    text = models.TextField(max_length=1500)
    image = models.ImageField(upload_to='blog_images/')

    def get_summary(self):
        if len(self.text) > 100:
            return self.text[:100] + "..."
        else:
            return self.text

    def __str__(self):
        return self.title



