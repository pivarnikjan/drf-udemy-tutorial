from django.contrib import admin

from drf_profile import models

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
