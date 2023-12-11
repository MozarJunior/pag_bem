from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Admin(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=10)

    def __str__(self):
        return self.nome

class Estabelecimento(models.Model):
    nome = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    senha = models.CharField(max_length=20)
    ativo = models.BooleanField()
    criadoEm = models.DateTimeField(auto_now_add=True)
    atualizadoEm = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class EstabelecimentoCliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, null=True)
    ingresso = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente.nome + ' - ' + self.estabelecimento.nome

class Plano(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.FloatField()
    duracaoDias = models.IntegerField()
    frequencia = models.IntegerField()
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.nome + ' - ' + self.estabelecimento.nome

class PlanoControle(models.Model):
    ingresso = models.DateTimeField(auto_now_add=True)
    vencimento = models.DateTimeField(auto_now_add=True)
    plano = models.ForeignKey(Plano, on_delete=models.SET_NULL, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.cliente.nome + ' - ' + self.plano.nome

