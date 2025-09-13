from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Function to check if user has Admin role
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin-only view
@user_passes_test(is_admin, login_url='login', redirect_field_name=None)
def admin_view(request):
    """
    View accessible only to users with the Admin role.
    """
    return render(request, 'relationship_app/admin_view.html')
