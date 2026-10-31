import csv
import time
from src.original import sugerir
from src.trie import Trie
from src.dados import gera_palavras, gera_prefixos

def mede(funcao, repeticoes=3):
    melhor = float('inf')
    for _ in range(repeticoes):
        ini = time.perf_counter()
        funcao()
        melhor = min(melhor, time.perf_counter() - ini)
    return melhor

TAMANHOS = [1_000, 10_000, 100_000, 500_000]
linhas = []

for n in TAMANHOS:
    palavras = gera_palavras(n)
    prefixos = gera_prefixos(palavras, qtd=100)

    t_orig = mede(lambda: [sugerir(palavras, p) for p in prefixos])
    t_build = mede(lambda: Trie(palavras))
    trie = Trie(palavras)
    t_trie = mede(lambda: [trie.sugerir(p) for p in prefixos])

    linhas.append([n, t_orig, t_build, t_trie])
    print(f"n={n:>8} | original={t_orig:.4f}s | construcao={t_build:.4f}s | trie={t_trie:.4f}s")

with open("benchmarks/resultados.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["n", "original_s", "construcao_trie_s", "consulta_trie_s"])
    w.writerows(linhas)