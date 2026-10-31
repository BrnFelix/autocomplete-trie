# Autocompletar por Prefixo - Otimização de Código

Projeto de Análise e Otimização de Sistemas (UniJorge) - Prof. Igor Gonzalez

Integrantes: Bruno Felix, Camila Ellen, Rafael Faria

## O que o projeto faz

Compara duas formas de sugerir palavras a partir de um prefixo:
- Original: varre toda a lista de palavras a cada consulta, com custo O(n·k)
- Otimizada: usa uma trie (árvore de prefixos), com custo O(k + r)

## Como executar
    pip install pytest matplotlib
    python -m pytest -v
    python -m benchmarks.benchmark
    python benchmarks/grafico.py
