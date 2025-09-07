from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# Helper functions for role checks
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"


# Views restricted by role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "admin_view.html")


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "librarian_view.html")


@user_passes_test(is_member)
def member_view(request):
    return render(request, "member_view.html")
