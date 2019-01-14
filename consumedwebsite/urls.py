"""consumedwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import releases.views
import support.views
import radio.views
import press.views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', releases.views.home, name='home'),
    path('contact/', releases.views.contact, name='contact'),
    path('press/', press.views.press, name='press'),
    path('radio/', radio.views.radio, name='radio'),
    path('releases/', releases.views.allreleases, name='releases'),
    path('support/', support.views.support, name='support'),
    path('<int:release_id>', releases.views.details, name = 'detail'),
    path('radio/<int:radio_id>', radio.views.radiodetails, name = 'radiodetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
