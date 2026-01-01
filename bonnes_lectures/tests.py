from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import Book
from .utils.isbn import Isbn

class IsbnUnitTests(TestCase):
    """Tests unitaires pour la classe utilitaire Isbn."""

    def test_isbn_valide(self):
        """Vérifie qu'un ISBN correct est accepté."""
        code = "978-2-070-54022-8" 
        isbn = Isbn(code)
        self.assertTrue(isbn.is_valid())
        self.assertEqual(str(isbn), "978-2-070-54022-8")

    def test_isbn_nettoyage(self):
        """Vérifie que les tirets et espaces sont bien ignorés."""
        code = "978 2 070-54022 8" 
        isbn = Isbn(code)
        self.assertTrue(isbn.is_valid())

    def test_isbn_invalide_longueur(self):
        """Vérifie qu'un code trop court/long lève une erreur."""
        with self.assertRaises(ValidationError):
            Isbn("12345") 

    def test_isbn_invalide_checksum(self):
        """Vérifie qu'une clé de contrôle fausse lève une erreur."""
        code = "978-2-070-54022-0" 
        with self.assertRaises(ValidationError):
            Isbn(code)

class BookModelTests(TestCase):
    """Tests d'intégration pour le modèle Book et son champ IsbnField."""

    def setUp(self):
        self.user = User.objects.create_user(username='testeur', password='pw')

    def test_create_book_valid_isbn(self):
        """On doit pouvoir sauver un livre avec un bon ISBN."""
        book = Book(
            title="Livre Test",
            year=2024,
            publisher="Editions Test",
            backCover="Résumé...",
            isbn="978-2-070-54022-8",
            user=self.user
        )
        try:
            book.full_clean() 
            book.save()
        except ValidationError:
            self.fail("Le livre avec un ISBN valide a été rejeté !")

    def test_create_book_invalid_isbn(self):
        """Un livre avec un mauvais ISBN doit être rejeté."""
        book = Book(
            title="Livre Faux",
            year=2024,
            publisher="Editions Test",
            backCover="Résumé...",
            isbn="978-2-070-54022-0", # Clé invalide
            user=self.user
        )
        with self.assertRaises(ValidationError):
            book.full_clean()