from django.contrib import admin

from .models import Follower, Following, Blockuser
# Register your models here.

admin.site.register(Follower)
admin.site.register(Following)
admin.site.register(Blockuser)
