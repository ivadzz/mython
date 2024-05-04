
import random as r
lista = []
for i in range(100):
    n = r.randint(0,100)
    lista.append(n)
print(len(lista))
with open("lista_n_ord.txt","w") as f:
    for i in range(len(lista)):
        f.write("{} ".format(lista[i]))
    f.close()
