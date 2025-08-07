"""
URL configuration for periodtracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from health import views
from health.views import Contact


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('index.html',views.index),
    path('symptoms.html',views.symptoms),
    path('healthtips.html',views.healthtips),
    #path('contact.html', views.contact, name='contact'),
    path('Contact', views.Contact, name='Contact'),

]


    #path('contact.html/',views.contact),
    #path('doctores.html/',views.doctores),
    #path('about.html/',views.about),
    #path('healthtips.html/',views.healthtips),
    #path('symptoms.html/',views.symptoms),
