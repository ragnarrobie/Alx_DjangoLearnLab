from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required. Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'avatar']  # include avatar only if ImageField is used

from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']   # only content is entered by the user
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your content...'}),
        }
from django import forms
from .models import Post
from taggit.forms import TagWidget  # import the widget from django-taggit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your content...'}),
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'}),
        }
from django import forms
from .models import Post
from taggit.forms import TagWidget  # import TagWidget from django-taggit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'rows': 8, 'placeholder': 'Write your content...'}),
            'tags': TagWidget(attrs={'placeholder': 'Add tags separated by commas'}),  # TagWidget here
        }
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags'] # 'tags' is automatically handled by django-taggit
        widgets = {
            # This just adds a placeholder to the default text input for tags
            'tags': forms.TextInput(attrs={'placeholder': 'Comma-separated tags'}),
        }