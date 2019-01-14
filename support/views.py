from django.shortcuts import render

from .models import Support, Supportimage


# Create your views here.

def support(request):
	supports = Support.objects
	screenshots = Supportimage.objects
	return render(request, 'support/support.html',{'support':supports, 'supportimage':screenshots,})
