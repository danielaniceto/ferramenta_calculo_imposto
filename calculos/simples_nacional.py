import json
from app.models import *

class CalculoSimplesNacional:       
    #Anexo 01 - Comercio
    def calcular_simples_nacional_menor_180k(self, imposto_simples_nacional: SimplesNacional):
        imposto_simples_nacional.receita_bruta
        imposto_simples_nacional.porcentagem_alicota 
        imposto_simples_nacional.faixa_desconto

        if imposto_simples_nacional.receita_bruta <= 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")
        
        elif 0 < imposto_simples_nacional.receita_bruta <= 180000:
            imposto_anexo01_menor_180k = (imposto_simples_nacional.receita_bruta * imposto_simples_nacional.porcentagem_alicota) - imposto_simples_nacional.faixa_desconto
            return imposto_anexo01_menor_180k

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
        sort_keys=True, indent=4)
