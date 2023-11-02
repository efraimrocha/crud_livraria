from django import forms
from .models import Book

# modelForm

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','publication_year']
        