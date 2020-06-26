from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Note
from rest_framework.authtoken.admin import TokenAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Book)
admin.site.register(Note)
TokenAdmin.raw_id_fields = ['user']