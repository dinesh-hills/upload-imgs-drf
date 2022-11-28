from django.db import models

# Create your models here.
class UploadImages(models.Model):
    image = models.ImageField(upload_to='images')