valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
valor=float(input())
if valor < 0:
  print("impossível")
else:
  for i in range(len(valores)):
    qnt = valor // valores[i]
    valor = valor - qnt*valores[i]
    if valores[i] >= 1:
      print("{:.0f} Nota(s) de R$ {:.2f}".format(qnt,valores[i]))
    else:
      print("{:.0f} Moeda(s) de R$ {:.2f}".format(qnt,valores[i]))
    i+=1
