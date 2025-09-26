from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # List + detail
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # Create
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # Update (two options: with ID or generic /books/update)
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/update/', BookUpdateView.as_view(), name='book-update-no-id'),

    # Delete (two options: with ID or generic /books/delete)
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete-no-id'),
]
