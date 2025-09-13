# Retrieve Operation

# retrieve the book created earlier

from bookshelf.models import Book
b = Book.objects.get(pk=1) # or use b = Book.objects.get(pk=book.pk) if running in same shell
(b.title, b.author, b.publication_year)

# Expected output:

# ('1984', 'George Orwell', 1949)
