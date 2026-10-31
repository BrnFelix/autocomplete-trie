from src.original import sugerir
from src.trie import Trie
from src.dados import gera_palavras, gera_prefixos

def compara(palavras, prefixo):
    esperado = sorted(set(sugerir(palavras, prefixo)))
    obtido = sorted(Trie(palavras).sugerir(prefixo))
    assert esperado == obtido

def test_sem_correspondencia():
    compara(["casa", "carro"], "zzz")

def test_prefixo_vazio():
    compara(["casa", "carro", "boi"], "")

def test_prefixo_igual_a_palavra():
    compara(["casa", "casamento", "casaco"], "casa")

def test_repetidas():
    compara(["casa", "casa", "caso"], "ca")

def test_dicionario_vazio():
    compara([], "a")

def test_aleatorio():
    palavras = gera_palavras(5000)
    for pre in gera_prefixos(palavras, qtd=300):
        compara(palavras, pre)