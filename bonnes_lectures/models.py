from django.db import models
from django.contrib.auth.models import User
from .fields import IsbnField

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    
    authors = models.ManyToManyField(Author, related_name='books')
    
    publisher = models.CharField(max_length=200)
    year = models.IntegerField()
    isbn = IsbnField(unique=True)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(
        choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')]
    )

    def __str__(self):
        return f"Avis de {self.user} sur {self.book.title}"