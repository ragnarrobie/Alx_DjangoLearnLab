from rest_framework import serializers
from .models import Author, Book
import datetime


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    Includes custom validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure the publication year is not greater than the current year."""
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future (>{current_year})."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.
    Includes a nested BookSerializer to represent all books written by the author.
    """
    books = BookSerializer(many=True, read_only=True)  
    # uses related_name='books' in Book model

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
