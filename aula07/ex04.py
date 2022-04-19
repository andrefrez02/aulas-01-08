from operator import neg


print('Escreva um algoritmo que leia um grupo de valores reais e determine quantos',
      'valores são positivos e quantos são negativos. Determine, também, qual é o',
      'menor desses valores. Utilize o comando de repetição que desejar.')
val = []
c = 0
val.append(float(input('\nEntrada:\nDigite um valor para o 1° número: ')))
sair = 'n'
while sair not in 'Ss':
    c += 1
    sair = input('Digite "S" para sair ou digite qualquer coisa para continuar inserindo números: ')
    if sair not in 'Ss':
        val.append(float(input(f'Digite um valor para o {c + 1}° número: ')))
print(f'\nSaída:\nValores digitados: [', end = '')
neg, pos, maior, menor, c2 = 0, 0, 0, 0, 0
for i in val:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    if i > 0:
        pos += 1
    if i < 0:
        neg += 1
    print(f'{val[c2]}', end = ', ')
    c2 += 1
print(f'\b\b].\nSendo [{maior}, {menor}] respectivamente o maior e o menor número entre eles.\n{pos} desses números são positivos e {neg} são negativos.')