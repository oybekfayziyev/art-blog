from django.contrib import admin
from .models import Post,PostExtraImage
# Register your models here.

class ItemImageInline(admin.TabularInline):
	model = PostExtraImage
	extra = 5

class PostAdmin(admin.ModelAdmin):
     
    list_display = [
        'user',
        'image',
        'content',
        'slug'
    ]  

    list_display_links = [
		'user',
		'slug'
	]

    list_filter = [
        'user',
        'content',
   
    ]
    
    search_fields = [
        'user__username'
    ]
    inlines = [ItemImageInline]

admin.site.register(Post,PostAdmin)