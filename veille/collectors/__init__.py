"""Connecteurs de collecte. Chaque connecteur renvoie une liste d'éléments bruts normalisés :
{url, titre, auteur, resume_source, publie_le, langue, origine, donnees, [url_canonique]}."""


class CollectorError(Exception):
    """Erreur de collecte propre à une source (flux mal formé, réponse inattendue)."""


class NotConfigured(CollectorError):
    """Le connecteur nécessite une configuration (jeton, compte) absente."""
