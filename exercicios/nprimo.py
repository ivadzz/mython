def ehprimo(a):
    if a < 2:
        return False  # Números menores que 2 não são primos
    elif a == 2:
        return True  # 2 é o único número par que é primo
    elif a % 2 == 0:
        return False  # Números pares maiores que 2 não são primos
    else:
        # Testar somente até a raiz quadrada de 'a'
        from math import isqrt  # Função para raiz quadrada inteira
        for i in range(3, isqrt(a) + 1, 2):
            if a % i == 0:  # Se divisível por qualquer número, não é primo
                return False
        return True  # Se nenhum divisor for encontrado, o número é primo

a=int(input())
if ehprimo(a):
    print("true")
else:
    print("false")

 

