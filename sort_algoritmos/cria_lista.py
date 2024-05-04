import random as r
lista = []
for i in range(300):
    n = r.randint(0,1000)
    lista.append(n)
print(len(lista))
print(lista)
with open("lista_n_ord.txt","w") as f:
    for i in range(len(lista)):
        f.write("{} ".format(lista[i]))
