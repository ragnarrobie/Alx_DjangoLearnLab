# Delete Operation

from bookshelf.models import Book
b = Book.objects.get(pk=1)
b.delete()

# Expected delete output (example):

# (1, {'bookshelf.Book': 1})

# confirm deletion

Book.objects.all()

# Expected output:

# <QuerySet []>
