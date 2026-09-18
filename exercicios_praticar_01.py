""" Exercícios para praticar Python - 01

# 1. Faça um programa que leia um número inteiro e imprima-o."""

print('Exercício 01')
numero_inteiro = int(input("Digite um número inteiro: "))
print(f'Você digitou o numero inteiro: {numero_inteiro} ')

# 2- Faça um programa que peça para o usuário digitar três valores inteiro e imprima a soma deles.

print('Exercício 02')

print('Digite três valores inteiro')
valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
valor_3 = int(input("Digite o terceiro valor: "))
soma = valor_1 + valor_2 + valor_3
print(f'A soma dos três valores inteiros que você digitou é: {soma} ')

# 3 - Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.
print('Exercício 03')
print('Digite três valores')
valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
valor_3 = int(input("Digite o terceiro valor: "))

soma_dos_quadrados = (valor_1)**2 + (valor_2)**2 + (valor_3)**2
print(f'A soma dos quadrados dos três valores que você digitou é: {soma_dos_quadrados} ')