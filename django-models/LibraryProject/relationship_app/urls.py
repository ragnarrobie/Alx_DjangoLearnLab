from django.urls import path
from .import views
from .views import list_books
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="relationship_app/login.html"),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"),name="logout"),
    path('register/',views.register,name="register"),
    path('',views.list_books,name="list_books"),
    path('',views.LibraryDetailView.as_view(),name="Library_detail")
]