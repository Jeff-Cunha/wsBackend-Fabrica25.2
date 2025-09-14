from django.db import models

# Create your models here.

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100, unique=True, help_text="Nome do ingrediente")

    def __str__(self):
        return self.nome
    
class Receitas(models.Model):
    nome_receita = models.CharField(max_length=100, unique=True, help_text="Nome da receita")
    passos = models.TextField(help_text="Passos para fazer a receita")
    tempo_preparo = models.IntegerField(help_text="Tempo de preparo em minutos")
    ingredientes = models.ManyToManyField(Ingrediente, help_text="Ingredientes da receita")

    def __str__(self):
        return self.nome_receita