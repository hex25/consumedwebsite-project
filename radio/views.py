from django.shortcuts import render, get_object_or_404

from .models import Radio

# Create your views here.

def radio(request):
	radios = Radio.objects
	return render(request, 'radio/radio.html',{'radio':radios})

def radiodetails(request, radio_id):
	detailpodcast = get_object_or_404(Radio, pk=radio_id)
	return render(request, 'radio/radiodetail.html', {'radio': detailpodcast})
