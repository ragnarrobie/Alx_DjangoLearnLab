from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints.
    Tests cover CRUD, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create sample Author and Book
        self.author = Author.objects.create(name="George Orwell")
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

    # ---------- READ TESTS ----------
    def test_list_books(self):
        """Ensure books list is accessible to all users."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_get_single_book(self):
        """Ensure a single book can be retrieved."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    # ---------- CREATE TESTS ----------
    def test_create_book_requires_authentication(self):
        """Ensure unauthenticated users cannot create a book."""
        data = {"title": "Animal Farm", "publication_year": 1945, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a book."""
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "Animal Farm", "publication_year": 1945, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest("id").title, "Animal Farm")

    # ---------- UPDATE TESTS ----------
    def test_update_book_requires_authentication(self):
        """Ensure unauthenticated users cannot update a book."""
        data = {"title": "1984 Updated", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Ensure authenticated users can update a book."""
        self.client.login(username="testuser", password="testpass123")
        data = {"title": "1984 Updated", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "1984 Updated")

    # ---------- DELETE TESTS ----------
    def test_delete_book_requires_authentication(self):
        """Ensure unauthenticated users cannot delete a book."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        """Ensure authenticated users can delete a book."""
        self.client.login(username="testuser", password="testpass123")
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    # ---------- FILTERING, SEARCHING, ORDERING ----------
    def test_filter_books_by_year(self):
        """Ensure filtering works by publication_year."""
        response = self.client.get(f"{self.list_url}?publication_year=1949")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_search_books_by_title(self):
        """Ensure searching works by title."""
        response = self.client.get(f"{self.list_url}?search=1984")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("1984", str(response.data))

    def test_order_books_by_year(self):
        """Ensure ordering works by publication_year."""
        Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # First book should be Animal Farm (1945)
        self.assertEqual(response.data[0]["title"], "Animal Farm")
