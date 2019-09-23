from django.db import models
from datetime import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(null=False, max_length=50)
    date = models.DateField(null=False,default=datetime.now)
    paragraph = models.CharField(null=False, max_length=150)
    image = models.ImageField(null=True,upload_to='post_pictures', default='')

    def __str__(self):
        return str(self.id) + " " + self.title
