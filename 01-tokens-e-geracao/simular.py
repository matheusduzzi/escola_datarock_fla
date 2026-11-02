"""Microlaboratório fictício, sem modelo treinado, rede ou credenciais."""
import json
import math
from pathlib import Path


def temperar(probabilidades, temperatura):
    if not math.isfinite(temperatura) or temperatura <= 0:
        raise ValueError('A temperatura deve ser finita e positiva.')
    if (not probabilidades or any(not math.isfinite(p) or p < 0 for p in probabilidades)
            or not math.isclose(sum(probabilidades), 1.0)):
        raise ValueError('Probabilidades finitas, não negativas e soma 1 são necessárias.')
    logs = [math.log(p) / temperatura if p else -math.inf for p in probabilidades]
    maior = max(logs)
    pesos = [math.exp(x - maior) for x in logs]
    return [p / sum(pesos) for p in pesos]


def escolher(probabilidades, u):
    if not 0 <= u < 1:
        raise ValueError('u deve estar em [0,1).')
    acumulada = 0
    for i, p in enumerate(probabilidades):
        acumulada += p
        if u < acumulada:
            return i
    return len(probabilidades) - 1


def segmentar(texto, vocabulario):
    # Maior peça compatível primeiro. Não implementa BPE nem tokenizer de produto.
    pecas = sorted(vocabulario, key=len, reverse=True)
    ids = []
    while texto:
        peca = next((p for p in pecas if texto.startswith(p)), None)
        if peca is None:
            raise ValueError('Texto fora do vocabulário didático.')
        ids.append(vocabulario[peca])
        texto = texto[len(peca):]
    return ids


def demonstrar():
    dados = json.loads((Path(__file__).parent / 'dados/caso.json').read_text())
    vocab = dados['vocabulario']
    ids = segmentar(dados['texto'], vocab)
    inverso = {v: k for k, v in vocab.items()}
    print('SIMULAÇÃO DIDÁTICA: sem modelo treinado; dados fictícios.')
    print('Texto:', repr(dados['texto']))
    print('Peças:', [inverso[i] for i in ids])
    print('IDs:', ids)
    print('Reconstrução:', repr(''.join(inverso[i] for i in ids)))
    print('Candidatos:', dados['candidatos'])
    for t in dados['temperaturas']:
        probs = temperar(dados['probabilidades'], t)
        saidas = [dados['candidatos'][escolher(probs, u)] for u in dados['uniformes']]
        print('T=%g | probabilidades=%s | escolhas=%s' %
              (t, ', '.join('%.2f%%' % (100*p) for p in probs), saidas))
    print('u fixos:', dados['uniformes'], '(não são frequências estimadas)')


if __name__ == '__main__':
    demonstrar()
