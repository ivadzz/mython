with open("jogos.txt","r") as f:
    linhas = f.readlines()
    linha1 = int(linhas[0])


with open("jogosSaida.txt","w") as f:

    for i in range(linha1):
        linha         = linhas[i+1].split()
        Horainicio    = int(linha[0])
        Minutoinicio  = int(linha[1])
        Horafim       = int(linha[2])
        Minutofim     = int(linha[3])

        inicio        = Horainicio*60+Minutoinicio
        fim           = Horafim*60+Minutofim

        if inicio > fim:
            duracao   = (24 * 60 - inicio) + fim
        else:
            duracao   = fim-inicio

        
        horas         = duracao//60
        minutos       = duracao%60

        f.write("O jogo durou {} horas e {} minutos.\n".format(horas,minutos))

        i+=1
