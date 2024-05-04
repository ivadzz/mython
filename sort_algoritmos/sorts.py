def counting_sort(arr):
    # Passo 1: Encontrar o valor mínimo e máximo para definir o intervalo de contagem
    min_val = min(arr)
    max_val = max(arr)
    
    # Passo 2: Criar a lista de contagem para contar a frequência de cada número
    count = [0] * (max_val - min_val + 1)  # Inicializa a lista de contagem
    
    # Passo 3: Contar a frequência de cada número na lista original
    for num in arr:
        count[num - min_val] += 1  # Incrementar a contagem para cada número
    
    # Passo 4: Construir a lista ordenada usando a lista de contagem
    sorted_arr = []  # Lista para armazenar os elementos ordenados
    
    for i, c in enumerate(count):  # Iterar sobre a lista de contagem
        sorted_arr.extend([min_val + i] * c)  # Adicionar elementos conforme a contagem
    
    return sorted_arr  # Retorna a lista ordenada


def bubble_sort(arr):
    arr_copy = arr.copy()  # Criar uma cópia da lista original
    n = len(arr_copy)
    for i in range(n - 1):
        for j in range(0, n - 1 - i):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]  # Troca
    return arr_copy  # Retorna a lista ordenada


def bead_sort(arr):
    # Remove elementos negativos ou zero
    arr = [x for x in arr if x > 0]

    # Encontrar o valor máximo para saber o número de linhas na matriz
    max_val = max(arr)

    # Criar uma matriz de tamanho (máximo valor) x (tamanho do array)
    beads = [[0] * len(arr) for _ in range(max_val)]

    # Colocar as contas na matriz (uma coluna por elemento)
    for i, value in enumerate(arr):
        # Preencher a matriz com contas (1s) com base no valor
        for j in range(value):
            beads[j][i] = 1

    # Fazer as contas "cair" por gravidade
    for row in beads:
        # Contar quantas contas em cada linha
        count = sum(row)
        # "Empurrar" as contas para o final (deixar cair)
        row[:count] = [1] * count
        row[count:] = [0] * (len(arr) - count)

    # Construir a lista ordenada a partir da matriz
    sorted_arr = []
    # Percorrer as colunas e contar as contas
    for col in range(len(arr)):
        value = sum(row[col] for row in beads)  # Quantas contas na coluna
        sorted_arr.append(value)

    return sorted_arr  # Retorna a lista ordenada
