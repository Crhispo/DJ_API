from pickle import TRUE
from pyexpat import model
from django.db import models

# Create your models here.


class Compania(models.Model):
    """Model definition for Compañia."""
    id = models.AutoField(primary_key=TRUE,db_column='idCompania')
    nombre = models.CharField(max_length=50)
    sitioweb = models.URLField(max_length=100)
    fundacion = models.PositiveIntegerField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Compania."""

        verbose_name = 'Compania'
        verbose_name_plural = 'Companias'
        
