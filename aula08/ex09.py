print('Faça um programa que leia dez conjuntos de dois valores, o primeiro representando',
'o nome do aluno e o segundo representando a sua altura em centímetros. Encontre e exiba',
'o nome do aluno mais alto e sua altura; a média das alturas dessa turma.\n\nEntrada:')
cadastros_total, count0, count1, count2 = [], 0, -1, -1
inp0, inp1, fim = 0, False, False
while not fim == True:
    count0 += 1
    while not isinstance(inp0, str):
        count1 += 1
        if count1 == 0:
            inp0 = input(f'Digite o nome do {count0}° aluno: ')
        else:
            inp0 = input(f'Valor digitado é inválido!\nDigite novamente o nome do {count0}° aluno: ')
    while inp1 == False:
        count2 += 1
        if count2 == 0:
            inp1 = input(f'Digite a altura da {count0}° pessoa em cm: ')
        else:
            inp1 = input(f'Valor digitado é inválido!\nDigite novamente a altura da {count0}° pessoa em cm: ')
        try:
            inp1 = int(inp1)
        except:
            inp1 = False
    cadastros_total.append([[inp0], [inp1]])
    resp = input('Digite ["S" - Sair ou "N" - Não sair] para parar de cadastrar alunos: ')
    if not resp in 'Ss':
        fim = False
        inp0, inp1, count1, count2 = 0, False, -1, -1
    else:
        fim = True
    print('')

cc, count_soma = 0, 0
for i in cadastros_total:
    pessoa = cadastros_total[cc]
    num = pessoa[1]
    count_soma = count_soma + num[0]
    cc += 1
cc, mais_alto = 0, 0
for i in cadastros_total:
    pessoa = cadastros_total[cc]
    nomel = pessoa[0]
    altural = pessoa[1]
    nome = nomel[0]
    altura = altural[0]
    if cc == 0:
        mais_alto = altura
        mais_alto_nome = nome
    elif mais_alto < altura:
        mais_alto = altura
        mais_alto_nome = nome
    cc += 1
    
print(f'Saída:\nVocê cadastrou no total: {count0} alunos.')
print(f'Aluno mais alto é: {mais_alto_nome} com {mais_alto} cm de altura.')
print(f'A média das alturas da turma é de: {(count_soma / cc):.2f}.')

count_ex, imp, c_nome = 0, [], 0
extra = input('\nDeseja ver a lista completa de cadastros?[S/N]: ')
if extra in 'Ss':
    for i in cadastros_total:
        imp = cadastros_total[count_ex]
        imp1 = imp[0]
        imp2 = imp[1]
        c_nome = len(imp[0])
        count_ex += 1
        if count_ex >= 10:
            print(f'{count_ex}', end='')
        else:
            print(f'0{count_ex}', end='')
        print(f'° cadastro | Nome: {str(imp1[0])} | Altura: {imp2[0]} cm')