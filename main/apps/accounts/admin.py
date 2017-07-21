from django.contrib import admin

from main.apps.accounts.models import UserProfile


admin.site.register(UserProfile)
