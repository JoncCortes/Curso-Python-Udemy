# """
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.
# """
entrada = input('Digite um numero INTEIRO: ')

if entrada.isdigit():
    numero_int = int(entrada)
    par_impar = numero_int % 2 == 0
    par_impar_texto = 'Impar'

    if par_impar:
        par_impar_texto = 'Par'

    print(f'o numero {numero_int} é {par_impar_texto}')
    
else:
    print('Você não digitou um INTEIRO')