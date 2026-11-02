"""Cálculo real de cosseno sobre vetores didáticos; não gera embeddings."""
import json
import math
from pathlib import Path

def cosseno(a, b):
    if not a or len(a) != len(b):
        raise ValueError('Dimensões incompatíveis ou vetor vazio')
    if not all(math.isfinite(x) for x in list(a)+list(b)):
        raise ValueError('Coordenada não finita')
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    if na == 0 or nb == 0:
        raise ValueError('Vetor nulo sem direção')
    return sum(x*y for x, y in zip(a, b))/(na*nb)

def ordenar(vetor, trechos):
    saida = [dict(t, score=cosseno(vetor, t['vetor'])) for t in trechos]
    return sorted(saida, key=lambda t: (-t['score'], t['id']))

def carregar():
    return json.loads((Path(__file__).parent/'dados/casos.json').read_text())

if __name__ == '__main__':
    caso = carregar()['demo']
    print('SIMULAÇÃO: vetores manuais, sem modelo real')
    print(caso['pergunta'])
    for t in ordenar(caso['vetor'], caso['trechos']):
        print(f"{t['id']} | cosseno={t['score']:.3f} | {t['unidade']} | {t['estado']}")
