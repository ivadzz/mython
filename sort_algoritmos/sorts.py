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
    n = len(arr)  # Número de elementos na lista
    # Passar pelo array n-1 vezes
    for i in range(n - 1):
        # `swapped` para verificar se houve troca nesta passagem
        swapped = False
        # Percorrer o array até a posição que não precisa mais ser verificada
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Se elementos adjacentes estão fora de ordem, trocá-los
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Indicar que houve uma troca
        # Se nenhuma troca ocorreu nesta passagem, a lista está ordenada
        if not swapped:
            break  # Pode sair do loop
    return arr  # Retorna a lista ordenada

