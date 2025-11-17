from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.IntegerField()
    isbn = models.CharField(max_length=20, unique=True)
    backCover = models.TextField()
    cover = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(
        choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')]
    )
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Avis pour {self.book.title} - {self.rating} étoiles"