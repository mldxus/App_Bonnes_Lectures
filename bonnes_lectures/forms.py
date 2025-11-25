from django import forms
from .models import *
import datetime

class BookForm(forms.ModelForm):
   
    YEAR_CHOICES = [(r, r) for r in range(datetime.date.today().year, 1900, -1)]
    

    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Année de publication")

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'year', 'isbn', 'backCover']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']
        labels = {
            'first_name': 'Prénom',
            'last_name': 'Nom',
        }