from django import forms
from .models import *
import datetime

class BookForm(forms.ModelForm):
   
    YEAR_CHOICES = [(r, r) for r in range(datetime.date.today().year, 1900, -1)]
    year = forms.ChoiceField(choices=YEAR_CHOICES, label="Année de publication")

    class Meta:
        model = Book
        fields = ['title', 'authors', 'publisher', 'year', 'isbn', 'backCover']
        
        widgets = {'authors': forms.CheckboxSelectMultiple(), }

        help_texts = {
            'Saisissez un ISBN-13 valide (ex : 978-2-070-54022-7).',
        }

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