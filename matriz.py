import numpy as np


def ehprimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def contprimo(matrix):
    counts = {}
    for row in matrix:
        for num in row:
            if ehprimo(num):
                if num not in counts:
                    counts[num] = 1
                else:
                    counts[num] += 1
    return counts


with open('teste1.txt', 'r') as file:
    n = int(file.readline())
    data = [[int(x) for x in line.split()] for line in file]

matrix = np.array(data)

prime_counts = contprimo(matrix)

with open('saida1.txt', 'w') as file:
    for prime, count in prime_counts.items():
        file.write(f"{prime} {count}\n")
