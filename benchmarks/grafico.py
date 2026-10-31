import csv
import matplotlib.pyplot as plt

n, orig, build, trie = [], [], [], []
with open("benchmarks/resultados.csv") as f:
    for r in csv.DictReader(f):
        n.append(int(r["n"]))
        orig.append(float(r["original_s"]))
        build.append(float(r["construcao_trie_s"]))
        trie.append(float(r["consulta_trie_s"]))

plt.figure(figsize=(7, 4.5))
plt.plot(n, orig, "o-", label="Original (varredura linear)")
plt.plot(n, trie, "s-", label="Trie (consulta)")
plt.plot(n, build, "^--", label="Trie (construção, uma vez)")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Tamanho do dicionário (n)")
plt.ylabel("Tempo para 100 consultas (s)")
plt.title("Autocompletar por prefixo: original x trie")
plt.legend()
plt.grid(True, which="both", alpha=0.3)
plt.tight_layout()
plt.savefig("grafico_av2.png", dpi=200)
print("Gráfico salvo em grafico_av2.png")