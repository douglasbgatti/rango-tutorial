from django.contrib import admin
from rango.models import Category, Page, UserProfile



class PageAdmin(admin.ModelAdmin):
	fieldsets = [ 
		('Category', {'fields': ['category']}),
		('Title',	 {'fields': ['title']}),
		('URL', 	 {'fields':	['url']}),
		('Views',	 {'fields': ['views']}),

		]
	list_display = ('category', 'title', 'url', 'views')



class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}
		


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
