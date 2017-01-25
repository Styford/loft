from django.contrib import admin
from extUser.models import extUser
from django.contrib.auth.models import User
# Register your models here.


class extUserAdmin(admin.ModelAdmin):
    fields = ['secret_key', 'user_key',]
    list_filter = ['user_key']

admin.site.register(extUser, extUserAdmin)
