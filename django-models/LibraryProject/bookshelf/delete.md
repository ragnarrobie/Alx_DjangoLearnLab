# Delete Operation

from bookshelf.models import Book

# Retrieve the book

book = Book.objects.get(pk=1)

# Delete the book

book.delete()

# Expected output (example):

# (1, {'bookshelf.Book': 1})

# Confirm deletion

Book.objects.all()

# Expected output:

# <QuerySet []>
