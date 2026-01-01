from django.db import models

class Cover(models.Model):
    # L'ISBN sert de clé primaire (identifiant unique)
    isbn = models.CharField(max_length=20, primary_key=True)
    
    # Le format de l'image (png, jpeg, gif...)
    format = models.CharField(max_length=10)
    
    # L'image elle-même, encodée en texte (Base64)
    # TextField permet de stocker de très longues chaînes de caractères
    image_data = models.TextField()

    def __str__(self):
        return f"Cover for {self.isbn} ({self.format})"