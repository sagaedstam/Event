from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff', 'date_joined')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-date_joined',)

admin.site.register(MyUser, MyUserAdmin)



# from django.contrib import admin
# from .models import MyUser

# # Register your models here.

# admin.site.register(MyUser)
