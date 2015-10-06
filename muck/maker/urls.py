# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('muck.maker.views',
    url(r'^list/$', 'list', name='list'),
	url(r'^(?P<question_id>[0-9]+)/$', views.printout, name='printout'),
	url(r'^$', 'home', name='home'),
	url(r'^Prints/$', 'Prints', name='Prints'),
	url(r'^about_tools/$', 'about_tools', name='about_tools'),
	url(r'^about_curriculum/$', 'about_curriculum', name='about_curriculum'),
	url(r'^about_staff/$', 'about_staff', name='about_staff'),
	url(r'^watch/$', 'watch', name='watch'),
	url(r'^tips_3D/$', 'tips_3D', name='tips_3D'),
	url(r'^tips_laser/$', 'tips_laser', name='tips_laser'),
	url(r'^home/$', 'home', name='home'),
	url(r'^contact/$', 'contact', name='contact'),
	url(r'^upload/$', 'upload', name='upload')
)
