
from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class CustomUser_reg(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "name",
        "last_name",
        "city",
        "age",
        "designation",
        "exprience",
    ]
