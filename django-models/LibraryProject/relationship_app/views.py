from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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


# Create your views here.
