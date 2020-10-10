"""Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import projects.views
from django.conf import settings #need ed to shwo static files
from django.conf.urls.static import static #needed for static files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',projects.views.home,name='home' ), #landing page
    path('projects/<int:project_id>', projects.views.detail, name ='detail'), #save provided int into variable called project_id
    path('proj/', projects.views.proj, name='proj'), #proj homepage
    path('profile/',projects.views.profile, name='profile' ),
    path('contact/', projects.views.contact, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) #needed for static files

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #needed for IMG files