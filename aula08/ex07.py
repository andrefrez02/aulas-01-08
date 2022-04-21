print('Faça um programa que leia uma quantidade indeterminada de números positivos',
'menores que 100 e conte quantos deles estão nos seguintes intervalos: [0-25], [26-',
'50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um',
'número negativo.\nEntrada:')
tipo, resp, fim, c, val, c1, resp1 = False, 'x', False, 0, [], 0, 's'

while fim == False:
    while tipo == False:
        try:
            resp = int(resp)
            if (resp < 0) or (resp > 100):
                resp = ''
                tipo = False
        except:
            if not c == 0:
                resp = input(f'Valor digitado inválido!\nDigite novamente um valor para o {c1 + 1}° número da lista[0-100]: ')
            else:
                resp = input(f'Digite um valor para o {c1 + 1}° número da lista[0-100]: ')
                c += 1
        tipo = isinstance(resp, int)
    resp1 = input('Deseja continuar cadastrando valores?[S/N]: ')
    if resp1 in 'Nn':
        val.append(resp)
        fim = True
    else:
        val.append(resp)
        print('')
        c1 += 1
        resp, c, fim, tipo = '', 0, False, False 
c, v0, v1, v2, v3, v4, v5 = 0, 0, 0, 0, 0, 0, 0
print(f'Os números digitados são ', end = '')
for i in val:
    v0 = val[c]
    if v0 <= 25:
        v1 += 1
    elif v0 <= 50:
        v2 += 1
    elif v0 <= 75:
        v3 += 1
    else:
        v4 += 1
    v5 = val[c]
    if c == len(val) - 1:
        print(val[c], end = '.\n')
    else: 
        print(val[c], end = ', ')
    c += 1
print(f'\n{v1} desses valores estão entre [000-025].\n{v2} desses valores estão entre [026-050].\n',
f'\b{v3} desses valores estão entre [051-075].\n{v4} desses valores estão entre [076-100].\n')