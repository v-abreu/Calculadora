"""
Programa entrada dados
Descrição: módulo de um programa python que permite a entrada de dois numeros
autor: vania
data: 31/08/2022
versão:0.0.1
def entra_dados():
"""

def entrada_dados():
    i=0
    lista_entrada=[]
    while i<2:
        numero=float(input("\nDigite um elemento da sua lista: "))
        lista_entrada.append(numero)
        i+=1
    return lista_entrada