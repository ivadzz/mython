import numpy as np

tamanho_matriz = int(input("Informe o valor da matriz: "))

matriz_simetrica = np.zeros((tamanho_matriz, tamanho_matriz), dtype=int)
for indice_linha in range(tamanho_matriz):
    for indice_coluna in range(tamanho_matriz):
        matriz_simetrica[indice_linha, indice_coluna] = (indice_linha - indice_coluna) ** 2

multiplos_4 = np.unique(matriz_simetrica[matriz_simetrica % 4 == 0])
multiplos_4 = np.sort(multiplos_4)

somas_linhas = np.sum(matriz_simetrica, axis=1)
indice_menor_soma = np.argmin(somas_linhas)
menor_soma = somas_linhas[indice_menor_soma]

maiores_valores_colunas = np.max(matriz_simetrica, axis=0)

with open('/content/matrizSaida.txt', 'w') as arquivo_saida:
    arquivo_saida.write("Matriz:\n")
    arquivo_saida.write(str(matriz_simetrica) + "\n\n")
    arquivo_saida.write(f"A matriz tem {len(multiplos_4)} múltiplos de 4 que são: {multiplos_4.tolist()}\n")
    arquivo_saida.write(f"A linha com menor soma é a {indice_menor_soma} cuja soma é {menor_soma}\n")
    arquivo_saida.write(f"Os maiores valores de cada coluna são: {maiores_valores_colunas.tolist()}\n")