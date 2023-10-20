from django.contrib import admin

from .models import Profile, Follower, Status, Teams

admin.site.register(Profile)
admin.site.register(Teams)
admin.site.register(Status)
admin.site.register(Follower)