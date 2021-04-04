from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.

class CustomUserAdmin(UserAdmin):
	ordering = ('-id',)
	list_display_links = ('username', 'mobile')
	list_display = ['username', 'email', 'mobile', 'gender', 'first_name', 'last_name', 'role']
	search_fields = ['username','email', 'mobile', 'gender', 'first_name', 'last_name', 'role']
	# add_fieldsets = (
	# 	(None, {
	# 		'classes': ('wide', 'extrapretty'),
	# 		'fields': ('first_name', 'last_name', 'email', 'mobile', 'username', 'password1', 'password2' ),
	# 	}),
	# )
	fieldsets = [
		(None, {'fields': ('email', 'username', 'mobile', 'first_name', 'last_name', 'password',)}),
		('Personal info', {'fields': ('image','role', 'gender' )})]

class PostAdmin(admin.ModelAdmin):
		
	view_on_site = True
	fieldsets = [
		(None, {'fields': ['title','slug', 'text', 'author', 'tag', 'category']}),
		('Date information', {'fields': ['published_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'author', 'slug','published_date', 'created_date')
	list_filter = ['published_date']
	search_fields = ['title']
	filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("title",)}
	# readonly_fields=('slug',)


class CategoryAdmin(admin.ModelAdmin):
		
	# view_on_site = True
	fieldsets = [
		(None, {'fields': ['title','text','slug','parent']}),
		('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'text','slug','parent', 'created_date')
	# list_filter = ['published_date']
	search_fields = ['title']
	# filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("title",)}

class TagAdmin(admin.ModelAdmin):
		
	# view_on_site = True
	fieldsets = [
		(None, {'fields': ['title','text','slug']}),
		('Date information', {'fields': ['created_date'], 'classes': ['collapse']}),

	]
	
	list_display = ('title', 'text','slug','created_date')
	# list_filter = ['published_date']
	search_fields = ['title']
	# filter_horizontal = ('tag',)
	prepopulated_fields = {'slug':("title",)}

class AppoitmentAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name','text','date','slot']})

	]
	
	list_display = ('name', 'text','date','slot')

class UservisitedAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['user','url']})

	]
	
	list_display = ('user','url')
		


admin.site.register(User, CustomUserAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Appoitment,AppoitmentAdmin)
admin.site.register(Uservisited,UservisitedAdmin)