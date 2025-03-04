from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    data_nasc = models.DateField()
    
    def __str__(self):
        return self.nome
