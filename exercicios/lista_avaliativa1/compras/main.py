listas = []
listona = []
tododia = []
sabado = []
totais = {}
dic = {}

with open('compras.txt', 'r',encoding='utf-8') as f:
    for i in range(6):
        l = f.readline().split()
        listas.append(l)
        listona += l

for i in range(0, len(listona), 2):
    item = listona[i]
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1

for item, contagem in dic.items():
    if contagem == 6:
        tododia.append(item)
tododia.sort()

for linha in listas:
    for i in range(0, len(linha), 2):
        item = linha[i]
        quantidade = int(linha[i + 1])
        if item in totais:
            totais[item] += quantidade
        else:
            totais[item] = quantidade

for i in range(0, len(listas[5]), 2):
    item = listas[5][i]
    unico = True
    for j in range(5):
        if item in listas[j]:
            unico = False
            break
    if unico:
        sabado.append(item)

with open('comprasSaida.txt', 'w', encoding="utf-8") as f:
    f.write('{} são comprados todos os dias da semana.\n\n'.format(tododia))
    f.write('Totais comprados de cada produto:\n')
    for item, total in totais.items():
        f.write('{}: {}\n'.format(item,total))
    f.write('\nProdutos comprados só aos sábados:\n')
    for item in sabado:
        f.write('{}\n'.format(item))
