from django.db import models
class Image(models.Model):
    name=models.CharField(max_length=64)
    image=models.ImageField(upload_to='Training_images/')

# Create your models here.
