from django.contrib import admin
from django.contrib.auth.models import User as OldUser
from .models import User
# Register your models here.

admin.site.unregister(OldUser)
admin.site.register(User)