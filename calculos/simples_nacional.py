import json
from app.models import *

class CalculoSimplesNacional:
#Anexo 01 - Comercio
    def calcular_simples_nacional_menor_180k(self, imposto_simples_nacional_menor_180k: SimplesNacional):
        imposto_simples_nacional_menor_180k.receita_bruta
        imposto_simples_nacional_menor_180k.porcentagem_alicota
        imposto_simples_nacional_menor_180k.faixa_desconto

        if imposto_simples_nacional_menor_180k.receita_bruta <= 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")
            
        elif imposto_simples_nacional_menor_180k.receita_bruta > 0 and  imposto_simples_nacional_menor_180k.receita_bruta <= 180000:
            imposto_anexo01_menor_180k = (imposto_simples_nacional_menor_180k.receita_bruta * imposto_simples_nacional_menor_180k.porcentagem_alicota) - imposto_simples_nacional_menor_180k.faixa_desconto
            
            return imposto_anexo01_menor_180k
