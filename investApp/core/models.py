from django.db import models


class Invest(models.Model):
    """Essa classe cria uma instancia de Investimento"""
    id_invest = models.AutoField(primary_key=True)
    invest_type = models.CharField(
        max_length=150, verbose_name='Tipo de Investimento')
    investor = models.CharField(
        max_length=150, verbose_name='Investidor')
    created_at = models.DateField(
        null=True, blank=True, verbose_name='Data do Investimento')
    value_invest = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Valor do Investimento')
