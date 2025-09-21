from django.db import models

class Dossier(models.Model):
    STATUT_CHOICES = [
        ('termine', 'Terminé'),
        ('en_attente', 'En attente'),
    ]
    dosdef = models.CharField(max_length=20, default="aucun", blank=True, null=True)
    tef = models.CharField(max_length=20, default="aucun", blank=True, null=True)
    bon_caisse = models.CharField(max_length=20, default="aucun", blank=True, null=True)
    mandat_paiement = models.CharField(max_length=20, default="aucun", blank=True, null=True)
    numero = models.CharField(max_length=20, unique=True)
    dostype = models.CharField(max_length=50, default="aucun", blank=True, null=True)
    responsable = models.CharField(max_length=100)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')

    def __str__(self):
        return self.numero
