# Importar a função `counting_sort` do módulo especificado
from sorts import counting_sort as csort
from sorts import bubble_sort as bb
from sorts import bead_sort as bd

# Lista de entrada para ordenação

with open("lista_n_ord.txt","r") as f:
   linha = f.readline().strip()# Ler a linha e remover espaços extras

lista = [int(x) for x in linha.split()]  # Dividir e converter para inteiros


lista_ordenada = csort(lista)

print("LINHA: {}".format(linha))
print('\n\n')
print("LISTA: {}".format(lista))
print('\n\n')
print("LISTA ORDENADA: {}".format(lista_ordenada))  # Espera-se uma lista ordenada

with open("lista_ord.txt","w") as f:
   f.write(" ".join(map(str, lista_ordenada)))
   f.close()
