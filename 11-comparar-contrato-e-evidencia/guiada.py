"""Exemplo resolvido público, separado dos casos autônomos."""
import json
FONTE = 'G1: resposta em 3 dias úteis após cadastro completo.'
RESPOSTAS = [
 {'valor':3,'unidade':'dias úteis','condicao':'após cadastro completo'},
 {'valor':3,'unidade':'dias corridos','condicao':'após cadastro completo'}
]
if __name__ == '__main__':
    print(FONTE)
    for n, r in enumerate(RESPOSTAS,1):
        ok = r == {'valor':3,'unidade':'dias úteis','condicao':'após cadastro completo'}
        print('G1 tentativa=%d fato=%s' % (n, str(ok).lower()))
    print('Aceitas: 1/2. Replay sintético, sem chamada de modelo.')
