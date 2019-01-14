from django.shortcuts import render, get_object_or_404

from .models import Release

# Create your views here.

def home(request):
	releases = Release.objects.order_by('-catal_number')

	return render(request, 'releases/home.html', {'releases':releases})

def allreleases(request):
	releases = Release.objects.order_by('-catal_number')
	return render(request, 'releases/releases.html', {'releases':releases})

def contact(request):
	return render(request, 'releases/contact.html',)

def details(request, release_id):
	detailrelease = get_object_or_404(Release, pk=release_id)
	return render(request, 'releases/releasedetail.html', {'release': detailrelease})
