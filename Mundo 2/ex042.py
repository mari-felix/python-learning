c = 1
lista = []

while c != 4:
    lado = int(input(f'Digite o {c}º número: '))
    lista.append(lado)
    c += 1

a, b, c = lista[0], lista[1], lista[2]

if a < b + c and b < a + c and c < a + b:
    print('FORMAM TRIÂNGULO')
    if a == b and b == c:
        print('TIPO DE TRIÂNGULO: EQUILÁTERO')
    elif (a == b != c) or (a == c != b) or (c == b != a):
        print('TIPO DE TRIÂNGULO: ISÓSCELES')
    else:
        print('TIPO DE TRIÂNGULO: ESCALENO')
else:
    print('NÃO FORMAM TRIÂNGULO')