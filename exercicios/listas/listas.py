listas  = []
lista5  = []
listona = []
unicos  = []
pal_exi = []
dic     = {}
with open("listas.txt", "r",encoding="utf-8") as f:
  n1 = int(f.readline())
  for i in range(n1):
    l = f.readline().split()
    listas.append(l)
    listona += l

for palavra in listona:
  if palavra in dic:
    dic[palavra]+=1
  else:
    dic[palavra] = 1
pal_exi = set(listona)
print('Palavras existentes     = {}'.format(pal_exi))
print('Repetições              = {}'.format(dic))

for palavra, contagem in dic.items():
  if contagem == 1:
    unicos.append(palavra)
unicos.sort()
print("Unicos                  = {}".format(unicos))

for j in range(len(listas[4])):
  if listas[4][j] in listas[0]:
    pass
  else:
    lista5.append(listas[4][j])
  j+=1
print('Tem na 5ª mas não na 1ª = {}'.format(lista5))

with open("listasSaida.txt","w", encoding="utf-8") as f:
  f.write('Palavras existentes     = {}\n'.format(pal_exi))
  f.write('Repetições              = {}\n'.format(dic))
  f.write("Unicos                  = {}\n".format(unicos))
  f.write('Tem na 5ª mas não na 1ª = {}\n'.format(lista5))
  f.close()