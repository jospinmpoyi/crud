from django.db import models

# Create your models here.
class Faculte(models.Model):
    libfac = models.CharField(max_length=50,blank=True, null=True)

class Etudiant(models.Model):
    nom = models.CharField(max_length=50,blank=True, null=True)
    postnom = models.CharField(max_length=50,blank=True, null=True)
    prenom = models.CharField(max_length=50,blank=True, null=True)
    telephone = models.CharField(max_length=50,blank=True, null=True)
    faculte = models.ForeignKey(Faculte,on_delete=models.CASCADE)

