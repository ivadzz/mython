def CRIA():
    import random as r
    lista = []
    for i in range(100):
        n = r.randint(0,100)
        lista.append(n)
    print('{}\n'.format(len(lista)))
    with open("info_lista.txt","w") as f:
        for i in range(len(lista)):
            f.write("{} ".format(lista[i]))
        f.close()
    return CRIA


def ARRUMA():
# Importar a função `counting_sort` do módulo especificado
   from sorts import counting_sort as csort
   from sorts import bubble_sort as bb
   from sorts import bead_sort as bd

# Lista de entrada para ordenação

   with open("info_lista.txt","r") as f:
      linha = f.readline().strip()# Ler a linha e remover espaços extras

   lista = [int(x) for x in linha.split()]  # Dividir e converter para inteiros


   lista_ordenada = csort(lista)

   print("LINHA: {}".format(linha))
   print('\n')
   print("LISTA: {}".format(lista))
   print('\n')
   print("LISTA ORDENADA: {}\n".format(lista_ordenada))  # Espera-se uma lista ordenada

   with open("info_lista.txt","w") as f:
      f.write(" ".join(map(str, lista_ordenada)))
      f.close()
   return ARRUMA


def DETALHES():
  listas  = []
  listona = []
  unicos  = []
  pal_exi = []
  dic     = {}
  with open("info_lista.txt", "r",encoding="utf-8") as f:
  
      l = f.readline().split()
      listas.append(l)
      listona += l

  for palavra in listona:
    if palavra in dic:
      dic[palavra]+=1
    else:
      dic[palavra] = 1
  pal_exi = set(listona)
  print('Palavras existentes     = {}\n'.format(pal_exi))

  for palavra, contagem in dic.items():
    if contagem == 1:
      unicos.append(palavra)
  unicos.sort()
  print("Unicos                  = {}".format(unicos))

  with open("info_lista.txt","w", encoding="utf-8") as f:
    f.write('Palavras existentes     = {}\n'.format(len(pal_exi)))
    f.write('Repetições              = {}\n'.format(dic))
    f.write("Unicos                  = {}\n".format(unicos))
    f.write('unicos existentes       = {}'  .format(len(unicos)))
    f.close()
  return DETALHES