from django.db import models


class Client(models.Model):
    id_personne = models.IntegerField(primary_key=True)
    id_classe = models.IntegerField()
    id_naturel_it = models.IntegerField()
    id_pays = models.IntegerField()
    nature_client = models.CharField(max_length=50)
    etat = models.CharField(max_length=50)
    id_categorie_avoir = models.IntegerField()
    raison_sociale = models.IntegerField()
    matricule = models.CharField(max_length=50)

    def __str__(self):
        return self.matricule


class ComptesEspece(models.Model):
    id_compte = models.IntegerField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_depositaire = models.IntegerField()
    date_creation = models.DateTimeField()
    web = models.CharField(max_length=50)
    etat = models.CharField(max_length=50)


class ImputationsEspeces(models.Model):
    LIBELLE = (
        ('CHQU', 'CHQU'),
        ('VIREMENT', 'VIREMENT'),
    )

    id_imputation = models.IntegerField(primary_key=True)
    id_compte_espece = models.ForeignKey(ComptesEspece, on_delete=models.CASCADE,
                                              blank=True)
    montant = models.FloatField()
    sens = models.BooleanField()
    date_imputation = models.DateTimeField()
    id_date_imputation = models.IntegerField()
    id_sdb_compte = models.IntegerField()
    date_valeur = models.DateTimeField()
    nature = models.CharField(max_length=50)
    etat = models.IntegerField()
    date_etat = models.IntegerField()
    libelle = models.CharField(max_length=10, choices=LIBELLE)

    def __str__(self):
        return self.id_imputation
