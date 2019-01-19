"""opiti_inc URL Configuration

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
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'OPITI Incorporated'
admin.site.site_title = 'Opiti Inc Admin Portal'
admin.site.index_title = 'Welcome to Opiti Inc Portal'

urlpatterns = [
    path('', include(('opiticonsulting.urls','opitInc'), namespace='opitInc')),
    path('blog/', include('zinnia.urls')),
    path('comments/', include('django_comments.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
