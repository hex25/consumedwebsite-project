from django.db import models

# Create your models here.

class Press(models.Model):

    press_title = models.CharField(max_length=200)
    press_summary = models.TextField()
    press_image = models.ImageField(upload_to='images/')
    catal_number = models.CharField(max_length=20)
    release_link = models.CharField(max_length=100)
    press_link = models.CharField(max_length=100)
