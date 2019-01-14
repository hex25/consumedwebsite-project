from django.shortcuts import render

from .models import Press

# Create your views here.

def press(request):
	press_clippings = Press.objects
	return render(request, 'press/press.html',{'press':press_clippings})
