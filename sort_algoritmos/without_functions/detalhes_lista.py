listas  = []
listona = []
unicos  = []
pal_exi = []
dic     = {}
with open("lista_ord.txt", "r",encoding="utf-8") as f:
  
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

for palavra, contagem in dic.items():
  if contagem == 1:
    unicos.append(palavra)
unicos.sort()
print("Unicos                  = {}".format(unicos))

with open("lista_detalhada.txt","w", encoding="utf-8") as f:
  f.write('Palavras existentes     = {}\n'.format(len(pal_exi)))
  f.write('Repetições              = {}\n'.format(dic))
  f.write("Unicos                  = {}\n".format(unicos))
  f.write('unicos existentes       = {}'  .format(len(unicos)))
  f.close()
