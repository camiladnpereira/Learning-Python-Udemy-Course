""" Escopo de variaveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são conhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja,
    seu escopo está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel



numero = 42
print(numero)
print(type(numero))

numero = 'Geek'
print(numero)
print(type(numero))

"""

numero = 2
novo = 0
if numero > 10:
    novo = numero + 10
    print(novo)

print(novo)
