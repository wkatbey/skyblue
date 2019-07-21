from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(
        max_length=20, 
        verbose_name="Category"
    )

    description = HTMLField()

class MediaEntry(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    description = HTMLField()
    
    content = models.FilePathField()
    image_thumbnail = models.ImageField()

    date_of_upload = models.DateTimeField()
    categories = models.ManyToManyField(Category, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def get_absolute_url(self):
        return reverse('media:media-detail', args=[self.id])
