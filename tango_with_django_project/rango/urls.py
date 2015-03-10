from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),	
	#regular expression to look for any sequence of alphanumeric characters (e.g. a-z, A-Z, or 0-9) and the hyphen(-) before the trailing URL slash
	url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
	url(r'^register/$', views.register, name='register'),	
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^search/$', views.search, name='search'),
)