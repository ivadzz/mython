def cria_sim(n):
    mat = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            mat[i][j] = mat[j][i] = n - 1 - i if i!= j else 0
    return mat

n = int(input("Informe o numero: "))
matriz_sim = cria_sim(n)

for matriz in matriz_sim:
    print(matriz)

multiplos = []
for matriz in matriz_sim:
    for elem in matriz:
        if elem % 4 == 0:
            multiplos.append(elem)

print('A matriz tem {} multiplos de 4, que sao: {}'.format(len(multiplos),multiplos))

min_matriz = min(matriz_sim, key=sum)
min_matriz_sum = sum(min_matriz)
print(f"A linha com menor soma é a {matriz_sim.index(min_matriz) + 1} cuja soma é : {min_matriz_sum} ")

