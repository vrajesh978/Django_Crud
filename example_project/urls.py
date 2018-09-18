"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from crudapp import  views


urlpatterns = 	[
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'^index$',views.login,name='index'),
    url(r'^$',views.login),
    url(r'^login$',views.login,name='login'),
    url(r'^register$',views.register,name='register'),
    url(r'^users$',views.users,name='users'),
    url(r'^show$',views.show,name='show'),
    url(r'^edit/(?P<pk>\d+)$',views.edit,name='edit'),
    url(r'^update/(?P<pk>\d+)$',views.update,name='update'),
    url(r'^delete/(?P<pk>\d+)$',views.delete,name='delete'),
]
