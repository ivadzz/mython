def get_substrings(s):
    """Retorna todas as substrings de uma string"""
    substrings = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.add(s[i:j])
    return substrings

def common_substrings_count(s1, s2):
    """Conta o número de substrings comuns entre duas strings"""
    substrings1 = get_substrings(s1)
    substrings2 = get_substrings(s2)
    common_substrings = substrings1.intersection(substrings2)
    return len(common_substrings)

# Exemplo de uso
string1 = "abc"
string2 = "bca"

count = common_substrings_count(string1, string2)
print(f"Número de substrings comuns: {count}")
