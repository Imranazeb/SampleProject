from django.contrib import admin

from common.userauths.models import Profile, User


# USER_MODEL
class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "id", "username", "email", "phone_number", "is_active")
    list_editable = ("is_active",)


admin.site.register(User, UserAdmin)


# PROFILE_MODEL
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("thumbnail", "full_name", "id", "user", "email", "phone_number")


admin.site.register(Profile, ProfileAdmin)
