from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CsUserAdmin(UserAdmin):
    list_display = ('email','username','name','is_host','date_joined','last_login','is_active','is_staff','is_superuser')
    search_fields = ('email','username')
    readonly_fields = ('email','date_joined','last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(User,CsUserAdmin)
# Register your models here.
