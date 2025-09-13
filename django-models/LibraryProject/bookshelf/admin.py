from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser  # Import the custom user from accounts

# Register the CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth']

admin.site.register(CustomUser, CustomUserAdmin)


# Register Book model
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'added_by', 'published_date', 'created_at']
