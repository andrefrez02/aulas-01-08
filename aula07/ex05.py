print('Temos um grupo de pessoas. Escreva um programa em Python que leia o',
'sexo e a altura de cada pessoa, calcule e mostre a altura média das mulheres e',
'dos homens separadamente. Utilize o comando de repetição que desejar.\n\nEntrada:')
cadastros_total, count0, count1, count2 = [], 0, -1, -1
inp0, inp1, fim = '0', False, False
cadastros_mulheres, cadastros_homens, count_f, count_m = [], [], 0, 0
while not fim == True:
    count0 += 1
    while not inp0 in 'FfMm':
        count1 += 1
        if count1 == 0:
            inp0 = input(f'Digite o sexo da {count0}° pessoa[F/M]: ')
        else:
            inp0 = input(f'Valor digitado é inválido!\nDigite novamente o sexo da {count0}° pessoa[F/M]: ')
    while inp1 == False:
        count2 += 1
        if count2 == 0:
            inp1 = input(f'Digite a altura da {count0}° pessoa em metros: ')
        else:
            inp1 = input(f'Valor digitado é inválido!\nDigite novamente a altura da {count0}° pessoa em metros: ')
        try:
            inp1 = float(inp1)
        except:
            inp1 = False
    cadastros_total.append([[inp0], [inp1]])
    if inp0 in 'Ff':
        cadastros_mulheres.append(inp1)
        count_f += 1
    else:
        cadastros_homens.append(inp1)
        count_m += 1
    resp = input('Digite ["S" - Sair ou "N" - Não sair] para parar de cadastrar pessoas: ')
    if not resp in 'Ss':
        fim = False
        inp0, inp1, count1, count2 = '0', False, -1, -1
    else:
        fim = True
    print('')

soma_m, soma_f, c0, c1, extra = 0, 0, 0, 0, 'n'
for i in cadastros_homens:
    soma_m = soma_m + cadastros_homens[c0]
    c0 += 1
for i in cadastros_mulheres:
    soma_f = soma_f + cadastros_mulheres[c1]
    c1 += 1
print(f'Saída:\nVocê cadastrou no total: {count0} pessoas.\nSendo {count_m} homens e {count_f} mulheres.')
match count_m:
    case 0:
        print('Não há media de altura dos homens pois, nenhum homem foi cadastrado.')
    case default:
        print(f'A média de altura dos homens é de: {(soma_m / count_m):.2f}')
match count_f:
    case 0:
        print('Não há media de altura das mulheres pois, nenhuma mulher foi cadastrada.')
    case default:
        print(f'E a média de altura das mulheres é de: {(soma_f / count_f):.2f}')
count_ex, imp = 0, []
extra = input('\nDeseja ver a lista completa de cadastros?[S/N]:')
if extra in 'Ss':
    for i in cadastros_total:
        imp = cadastros_total[count_ex]
        imp1 = imp[0]
        imp2 = imp[1]
        count_ex += 1
        print(f'{count_ex}° cadastro | Sexo: {str(imp1[0]).capitalize()} | Altura: {imp2[0]:.2f} metros')