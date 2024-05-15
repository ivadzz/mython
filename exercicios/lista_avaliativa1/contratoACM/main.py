res = []

with open("contrato.txt", "r") as f:
    for linha in f: 
        partes = linha.split()
        num = partes[0]
        valor = partes[1]  
        lista = list(valor)

        if num == "0":
            break
        else:
            while num in lista:
                lista.remove(num)

            while lista and lista[-1] == '0':
                lista.pop()

            if len(lista)<1:
                lista.append('0')
            else:
                pass
        res.append(''.join(lista))            
            
with open('saidaContrato.txt','w') as f:
    for i in range (len(res)):
        f.write('{}\n'.format(res[i]))
