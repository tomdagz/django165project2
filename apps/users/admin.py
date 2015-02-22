from django.contrib import admin
from .models import User
from .actions import export_as_excel
# Register your models here.

# @admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name', 'last_name',)
    search_fields = ('username', 'email',)
    list_filter = ('is_superuser',)
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    actions = [export_as_excel]
    fieldsets = (
        ('User', {'fields':('username','password')}),
        ('Personal info', {'fields':('first_name', 'last_name', 'email', 'avatar',)}),
        ('Permissions', {'fields':('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',)})
    )
admin.site.register(User, UserAdmin)
