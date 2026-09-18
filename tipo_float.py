"""
Tipo float é também conhecido por tipo real, decimal.
(números com casas decimais)

Como a programação é baseada em inglês, o separador das casas decimais é ponto e não vírgula.
"""

valor = 1.44
print(valor)
print(type(valor))


#tipo = type(valor)
print(f'O tipo da variável "valor" é {type(valor)}')

#É possível fazer dupla atribuição.

valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor1))


res = int(valor)
print(res)
print(type(res))

#Números complexos

num_complex = 5j
print(num_complex)
print(type(num_complex))

num_complex = num_complex ** 2
print(num_complex)
