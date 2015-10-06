from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^entry/$', views.entry, name = 'entry'),
	url(r'^confirm/$', views.confirm, name = 'confirm'),
	url(r'^nextPrints/$', views.nextPrints, name = 'nextPrints'),
	url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
	url(r'^get_name/$', views.get_name, name = 'get_name'),
]