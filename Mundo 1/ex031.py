'''
Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0.50
por Km para viagens de até 200 Km e R$0.45 para viagens
mais longas.
'''

print('''
------------------------------------------------
|                  CVC VIAGENS                 |
------------------------------------------------
''')
distancia = int(input('Distância a pecorrer(km): '))

if distancia > 200:
    preço = distancia * .45
else:
    preço = distancia * .5
print('-' * 30)
print(f'Total a pagar: R${preço}')