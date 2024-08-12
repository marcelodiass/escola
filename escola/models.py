from django.db import models


class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)
    
    def __str__(self):
        return self.nome