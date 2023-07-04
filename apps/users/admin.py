from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# class UserModelAdmin(UserAdmin):
#     pass
#     list_display = ('id','name','email','is_active','created_at',)
#     # list_filter = ('name','is_admin',)


admin.site.register(User)