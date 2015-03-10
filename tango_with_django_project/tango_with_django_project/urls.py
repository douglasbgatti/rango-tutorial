from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),
)


# if debug true allows to access variables defined in settings.py
if settings.DEBUG:
	urlpatterns +=patterns('django.views.static',
		(r'^media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), 
	)




# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
	def get_success_url(self,request,user):
		return '/rango/'
