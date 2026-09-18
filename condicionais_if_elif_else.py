""" Estruturas condicionais 'if' (Se), 'else' (Senão), 'elif' (vem de 'else if' [Senão Se])

"""

idade = int(input('Digite um valor para idade: '))

if idade < 18:
    print('Menor de idade')
elif idade == 18:
    print('Maior de idade com exatos 18 anos')
else:
    print('Maior de idade')

