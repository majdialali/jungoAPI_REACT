#THis file if you want to manage users through Django's admin panel, register your model.
from django.contrib import admin
from .models import UserProfile

# Registers the UserProfile model in the admin panel
admin.site.register(UserProfile)
