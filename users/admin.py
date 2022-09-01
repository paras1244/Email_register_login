
from django.contrib import admin
from users.models import CustomUser

@admin.register(CustomUser)
class CustomUser_reg(admin.ModelAdmin):
    list_display = [
        "id",
        "email",
        "user_type",
        "last_login",
    ]
