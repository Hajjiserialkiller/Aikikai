from django.contrib import admin
from userauths.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'bio')

admin.site.register(User, UserAdmin)