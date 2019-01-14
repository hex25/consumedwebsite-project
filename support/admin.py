from django.contrib import admin

# Register your models here.

from .models import Support, Supportimage

admin.site.register(Support)

admin.site.register(Supportimage)
