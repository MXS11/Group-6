"""my_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.views.generic import TemplateView
#We Add the allauth urls and specify “include” on top of import
urlpatterns = [
   #We Configure Django templates and link to the urls:
    path('',
         TemplateView.as_view(template_name="index.html")),

    path('admin/', admin.site.urls),
    # We add the accounts path to the urls.py file.
    path('accounts/', include('allauth.urls'))
]
