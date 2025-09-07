from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
def list_books(request):
    books = Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books": books})
def register(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)  # log in the user after registration
                return redirect("list_books")  # redirect to any page you like
        else:
            form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})
    
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
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


# Create your views here.
