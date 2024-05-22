with open('/content/substring.txt', 'r') as f:
    linha = f.readlines()

casos = int(linha[0].strip())

resultado = []

for i in range(1, 2 * casos, 2):
    str1 = linha[i].strip()
    str2 = linha[i + 1].strip()

    len1 = len(str1)
    len2 = len(str2)
    dpjmatrix = [[0] * (len2 + 1) for j in range(len1 + 1)]
    maxjlength = 0

    for x in range(len1 + 1):
        for y in range(len2 + 1):
            if x == 0 or y == 0:
                dpjmatrix[x][y] = 0
            elif str1[x-1] == str2[y-1]:
                dpjmatrix[x][y] = dpjmatrix[x-1][y-1] + 1
                if dpjmatrix[x][y] > maxjlength:
                    maxjlength = dpjmatrix[x][y]
            else:
                dpjmatrix[x][y] = 0

    resultado.append(str(maxjlength))

with open('/content/saidaSubstring.txt', 'w') as f:
    for result in resultado:
        f.write(f"{result}\n")