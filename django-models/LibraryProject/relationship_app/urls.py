from django.urls import path
from .import views
urlpatterns = [
    path('',views.list_books,name="list_books"),
    path('',views.LibraryDetailView.as_view(),name="Library_detail")
]