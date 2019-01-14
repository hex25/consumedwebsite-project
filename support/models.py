from django.db import models

# Create your models here.


class Support(models.Model):

    support_title = models.CharField(max_length=200)
    support_summary = models.TextField()
    support_embed = models.TextField(blank=True)
    catal_number = models.CharField(max_length=20)
    release_link = models.CharField(max_length=100)

    def __str__(self):
        return self.support_title

class Supportimage(models.Model):

    support_title = models.CharField(max_length=200)
    support_summary = models.TextField()
    support_image = models.ImageField(upload_to='images/', blank=True)
    catal_number = models.CharField(max_length=20)
    release_link = models.CharField(max_length=100)
    
    def __str__(self):
        return self.support_title
