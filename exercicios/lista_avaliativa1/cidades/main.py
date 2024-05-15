with open("crescimento.txt","r") as f:
    linhas = f.readlines()
    linha1 = int(linhas[0])


    with open("saidaCrescimento.txt","w") as f:
        for i in range(linha1):
            cidade  = linhas[i+1].split()
            cidadeA = int(cidade[0])
            cidadeB = int(cidade[1])
            taxaA   = float(cidade[2])/100
            taxaB   = float(cidade[3])/100
            anos    = 0


            while cidadeA <= cidadeB:
                cidadeA = int(cidadeA + (cidadeA * taxaA))
                cidadeB = int(cidadeB + (cidadeB * taxaB))
                anos += 1

            
            if anos > 100:
                f.write("Mais de 1 seculo.\n")
            else:
                f.write(f"{anos} anos.\n")
            
