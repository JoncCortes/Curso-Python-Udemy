# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """

nome = input('Digite seu nome: ')
qts_letras = len(nome)
print(f'seu nome tem {qts_letras} Letras.')

try:
    if qts_letras <=  4:
        print('Seu nome é curto!')

    elif qts_letras >= 5 and qts_letras <= 6:
        print('Seu nome tem um tamanho comum!')

    elif qts_letras > 7:
        print('Seu nome é bem grande!')


except:
    pass