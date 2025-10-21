from django import forms
from .models import Book
import datetime

class BookForm(forms.ModelForm):
   
    YEAR_CHOICES = [(r, r) for r in range(datetime.date.today().year, 1900, -1)]
    

    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Année de publication")

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'year', 'isbn', 'backCover']