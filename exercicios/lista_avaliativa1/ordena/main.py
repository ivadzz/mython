with open("ordena.txt","r") as f:
    linha1 = int(f.readline())
    linhas = f.readlines()

with open('saidaOrdena.txt','w') as f:
    for i in range(linha1):
        linha = linhas[i]
        linha = linha.split()
        linha.sort(key=len,reverse=True)
        f.write(' '.join(linha) + '\n')        
