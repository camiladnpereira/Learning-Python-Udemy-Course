""" Tipo de dado Numérico """
from difflib import restore

numero = 42
print(numero)

soma = numero + 10
print(soma)

subtracao = numero - 20
print(subtracao)

multiplicacao = numero * numero
print(multiplicacao)

divisao = numero / 2 # / faz a divisão e retorna um numero real, ou seja, pode ser com casas decimais.
print(divisao)

divisao_inteiro = numero // 2 # // faz a divisão e retorna apenas o número inteiro.
print(divisao_inteiro )

modulo = numero % 2 # % - módulo retorna o resto da divisão do numero por 2.
print(modulo)

"""Em todo numero impar, o resto da divisão por dois vai ser 1.
# Em todo numero par, o resto da divisão por dois vai ser 0. """

potenciacao = numero ** 2 # ** - numero elevado ao expoente 2
print(potenciacao)

""" Em Python, o limite do número que poderá ser armazenado é o limite da memória do computador"""
grande_numero = numero ** 1000
print(grande_numero)
um_milhao = 1_000_000 # é possivel separar os zeros por underline.
print(um_milhao)
print(type(um_milhao))

num = 10
num += 1
print(num)
num = 1
num -= 1
print(num)
num = 1
num *= 2
print(num)

num = 1
num /= 4
print(num)
