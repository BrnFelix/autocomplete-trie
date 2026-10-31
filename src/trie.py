class No:
    __slots__ = ("filhos", "fim")
    def __init__(self):
        self.filhos = {}
        self.fim = False

class Trie:
    def __init__(self, palavras=()):
        self.raiz = No()
        for p in palavras:
            self.inserir(p)

    def inserir(self, palavra):
        no = self.raiz
        for c in palavra:
            no = no.filhos.setdefault(c, No())
        no.fim = True

    def sugerir(self, prefixo):
        no = self.raiz
        for c in prefixo:
            if c not in no.filhos:
                return []
            no = no.filhos[c]
        saida = []
        pilha = [(no, prefixo)]
        while pilha:
            atual, texto = pilha.pop()
            if atual.fim:
                saida.append(texto)
            for c, filho in atual.filhos.items():
                pilha.append((filho, texto + c))
        return saida