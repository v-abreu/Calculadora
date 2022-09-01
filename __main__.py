"""
Programa soma utilizando módulos
Descrição: um programa python modularizado que seja uma calculadora com as 
4 operações aritméticas com dois números e que tenha um módulo principal 
e um módulo - chamado aritmetico.py -
além de módulos que forneçam funções de entrada e saída de dados.
Autor: vania
data: 28/08/2022
versão: 0.0.2
"""

#execução programa

import entrada
import aritmetico
import saida

def main():
    lista = entrada.entrada_dados()
    
    soma = aritmetico.adicao(lista[0], lista[1])

    subtracao = aritmetico.subtracao(lista[0], lista[1])

    multiplicacao = aritmetico.multiplicacao(lista[0], lista[1])

    divisao = aritmetico.divisao(lista[0], lista[1])
    
    saida.impressora(soma, subtracao, multiplicacao, divisao, lista[0], lista[1])

if __name__ == "__main__":
    main()