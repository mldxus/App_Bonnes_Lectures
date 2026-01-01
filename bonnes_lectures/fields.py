from django.db import models
from django.core.exceptions import ValidationError
from .utils.isbn import Isbn

class IsbnField(models.CharField):
    """Champ Django personnalisé pour gérer un ISBN complet et validé."""

    description = "Champ ISBN validé (13 chiffres + clé de contrôle)"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 17  # 13 chiffres + 4 tirets potentiels
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        """Convertit la valeur en objet Isbn."""
        if isinstance(value, Isbn):
            return value
        if value is None:
            return None
        return Isbn(value)

    def get_prep_value(self, value):
        """Transforme l'objet Isbn avant enregistrement."""
        if isinstance(value, Isbn):
            return value.code
        return str(value)

    def validate(self, value, model_instance):
        """Validation spécifique de l'ISBN."""
        # Note : La validation structurelle (longueur, clé) est déjà faite 
        # dans to_python -> Isbn.__init__.
        # On passe la version string au parent pour qu'il vérifie max_length, etc.
        super().validate(str(value), model_instance)