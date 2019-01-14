from django.db import models

# Create your models here.

class Radio(models.Model):

    podcast_title = models.CharField(max_length=200)
    podcast_summary = models.TextField()
    podcast_embed = models.TextField(blank=True)

    def shortsummary(self):
        return self.podcast_summary[:200]

    def radiodetails(request, radio_id):
    	detailpodcast = get_object_or_404(Radio, pk=radio_id)
    	return render(request, 'radio/radiodetail.html', {'radio': detailpodcast})
