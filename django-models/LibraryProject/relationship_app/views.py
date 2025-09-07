from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Library
from django.views.generic import DetailView
def list_books(request):
    book = Book.objects.all()
    return render(request,"relationship_app/list_books.html",{"books": books})
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Create your views here.
