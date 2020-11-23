from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    particularidade = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    categoria = models.CharField(max_length=255)