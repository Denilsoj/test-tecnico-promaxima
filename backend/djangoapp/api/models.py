from django.db import models

class Medicine(models.Model):

    substance = models.TextField()
    cnpj = models.CharField(max_length=30)
    laboratory = models.TextField()