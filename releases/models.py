from django.db import models

# Create your models here.


class Release(models.Model):

    release_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    catal_number = models.CharField(max_length=20)
    beatport_link = models.CharField(max_length=300, null=True)
    itunes_link = models.CharField(max_length=300, null=True)
    spotify_link = models.CharField(max_length=300, null=True)
    deezer_link = models.CharField(max_length=300, null=True)
    soundcloud_link = models.CharField(max_length=300, null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to='images/')

    def shortsummary(self):
        return self.summary[:30]

    def details(request, release_id):
    	detailrelease = get_object_or_404(Release, pk=release_id)
    	return render(request, 'releases/releasedetail.html', {'release': detailrelease})

    def __str__(self):
        return self.catal_number
