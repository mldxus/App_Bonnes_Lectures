import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Isbn:
    """Représente un code ISBN et assure sa validation."""

    def __init__(self, code: str):
        """Initialise un ISBN à partir d'une chaîne."""
        # Nettoyage : on enlève les tirets et espaces
        self.code = code.replace('-', '').replace(' ', '')
        
        # Vérification du format (13 chiffres)
        if not re.fullmatch(r'\d{13}', self.code):
            raise ValidationError(_("ISBN doit contenir exactement 13 chiffres."), code="tailleCode")
            
        self.prefixe = self.code[:3]
        self.groupe = self.code[3:5]
        self.editeur = self.code[5:9]
        self.article = self.code[9:12]
        self.cle = self.code[12]

        if not self.is_valid():
            raise ValidationError(_("ISBN invalide (clé de contrôle incorrecte)."), code="incorrectCode")

    def is_valid(self) -> bool:
        """Vérifie la clé de contrôle (ISBN-13)."""
        total = 0
        for i, c in enumerate(self.code[:-1]):
            mult = 1 if i % 2 == 0 else 3
            total += int(c) * mult
        cle_calculee = (10 - (total % 10)) % 10
        return cle_calculee == int(self.cle)

    def __str__(self):
        """Retourne la forme standardisée de l’ISBN."""
        return f"{self.prefixe}-{self.groupe}-{self.editeur}-{self.article}-{self.cle}"

    def __int__(self):
        """Retourne la forme entière de l’ISBN."""
        return int(self.code)

    def __len__(self):
        """Retourne la longueur de la chaîne ISBN."""
        return len(str(self))