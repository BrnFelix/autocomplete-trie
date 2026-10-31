import random
import string

def gera_palavras(n, tam_min=3, tam_max=12, seed=42):
    rng = random.Random(seed)
    letras = string.ascii_lowercase
    return [''.join(rng.choices(letras, k=rng.randint(tam_min, tam_max)))
            for _ in range(n)]

def gera_prefixos(palavras, qtd=200, seed=7):
    rng = random.Random(seed)
    prefixos = []
    for _ in range(qtd):
        p = rng.choice(palavras)
        k = rng.randint(1, min(4, len(p)))
        prefixos.append(p[:k])
    return prefixos