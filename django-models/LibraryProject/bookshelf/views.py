from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# Admin view
@user_passes_test(is_admin, login_url='login', redirect_field_name=None)
def admin_view(request):
    return render(request, 'bookshelf/admin_view.html')


# Librarian view
@user_passes_test(is_librarian, login_url='login', redirect_field_name=None)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')


# Member view
@user_passes_test(is_member, login_url='login', redirect_field_name=None)
def member_view(request):
    return render(request, 'bookshelf/member_view.html')
