import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "George Orwell"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name {author_name}")

print("\n" + "-"*40 + "\n")
library_name = "Central Library"
# Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # <- This line
    print(f"Librarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with the name {library_name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")


print("\n" + "-"*40 + "\n")
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian 
    print(f"Librarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with the name {library_name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
