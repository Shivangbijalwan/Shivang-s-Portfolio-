from django.contrib import admin
from .models import Contact

admin.site.register(Contact)

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# This will show the User model under your app section
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
