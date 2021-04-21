from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserImage

class CsUserAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_name','gender','dob','date_joined','last_login','is_active','is_staff','is_superuser')
    search_fields = ('email','username')
    readonly_fields = ('date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,CsUserAdmin)
admin.site.register(UserImage)
# Register your models here.
