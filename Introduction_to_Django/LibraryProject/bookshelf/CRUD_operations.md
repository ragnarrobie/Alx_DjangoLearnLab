# CRUD Operations Summary

## Create

from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# -> <Book: 1984 by George Orwell (1949)>

## Retrieve

b = Book.objects.get(pk=book.pk)
(b.title, b.author, b.publication_year)

# -> ('1984', 'George Orwell', 1949)

## Update

b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.get(pk=b.pk).title

# -> 'Nineteen Eighty-Four'

## Delete

b.delete()

# -> (1, {'bookshelf.Book': 1})

Book.objects.all()

# -> <QuerySet []>
