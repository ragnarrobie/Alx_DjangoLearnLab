from django.db import models

class Author(models.Model):
    """
    Author model to represent a book author.
    Each author can have multiple books (one-to-many relationship).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model that stores details of a book.
    Each book is linked to a single author via ForeignKey.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',  # Enables reverse lookup: author.books.all()
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
