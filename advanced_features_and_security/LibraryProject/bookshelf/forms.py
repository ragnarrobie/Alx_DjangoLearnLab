from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # Fields users can edit
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'title': 'Book Title',
            'author': 'Author Name',
            'published_date': 'Date Published',
        }
        help_texts = {
            'title': 'Enter the title of the book.',
            'author': 'Enter the name of the author.',
            'published_date': 'Select the published date.',
        }
