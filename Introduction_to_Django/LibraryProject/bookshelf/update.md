# Update Operation

from bookshelf.models import Book
b = Book.objects.get(pk=1)
b.title = "Nineteen Eighty-Four"
b.save()

# verify

Book.objects.get(pk=1).title

# Expected output:

# 'Nineteen Eighty-Four'
