import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Page, Category

top_views = Page.objects.all()
top_views_order = Page.objects.order_by('-views')[:5]

for top_view in top_views:
	print top_view.title

for top_view in top_views_order:
	print top_view