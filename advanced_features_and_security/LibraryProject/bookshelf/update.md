# Update Operation

from bookshelf.models import Book

# Retrieve the book

book = Book.objects.get(pk=1)

# Update the title

book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update

book.title

# Expected output:

# 'Nineteen Eighty-Four'
