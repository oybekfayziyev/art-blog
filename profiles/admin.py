from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src={} height="50px" width="50px"/>'.format(obj.profile_pic.url))
		    
    image_tag.short_description = 'Image'

    list_display = ['user','first_name','last_name','profile_pic']

admin.site.register(Profile,ProfileAdmin)
