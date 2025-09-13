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
from django import forms
from .models import Book

# Form for the Book model
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
        }

# Example form for testing purposes
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', help_text='Enter your full name')
    email = forms.EmailField(label='Email Address', help_text='Enter a valid email')
    message = forms.CharField(widget=forms.Textarea, label='Message', help_text='Enter your message')
