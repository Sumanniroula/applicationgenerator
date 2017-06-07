from django.conf.urls import url,include
from .models import Template
from .import views



urlpatterns = [

   
    url(r'^$',views.home,name='home'), 
	 # //after clicking application generator in view form
    url(r'^home/$',views.home,name='home'), 
  	#for CV app
  	url(r'^template/(?P<template_id>[0-9]+)/$',views.contents,name='template'),

    url(r'^template/(?P<template_id>[0-9]+)/edit/$',views.edit,name='edit'),
    url(r'^template/(?P<template_id>[0-9]+)/generate/$',views.generate,name='template.generate'),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')), 



]
