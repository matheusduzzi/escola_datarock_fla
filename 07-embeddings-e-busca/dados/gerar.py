"""Fixtures autorais fixas. Sem aleatoriedade ou modelo de linguagem."""
import json
from pathlib import Path

def dados():
    return {
        'procedencia': 'Loja Exemplo fictícia; vetores atribuídos manualmente para fins didáticos; sem modelo real',
        'demo': {'pergunta': 'Até que horas retiro meu pedido na unidade Centro pela regra vigente?', 'vetor': [1, 0], 'trechos': [
            {'id': 'C-antiga', 'unidade': 'Centro', 'estado': 'substituida', 'texto': 'Retirada de pedidos no Centro até 16h. Versão substituída.', 'vetor': [1, 0]},
            {'id': 'C-vigente', 'unidade': 'Centro', 'estado': 'vigente', 'texto': 'Retirada de pedidos no Centro até 18h. Esta versão substitui C-antiga.', 'vetor': [0.8, 0.6]},
            {'id': 'F-vigente', 'unidade': 'Centro', 'estado': 'vigente', 'texto': 'O frete depende do endereço de entrega.', 'vetor': [0, 1]}]},
        'autonomo': {'pergunta': 'A retirada na unidade Norte exige agendamento pela regra vigente?', 'vetor': [0, 1], 'trechos': [
            {'id': 'S-agenda', 'unidade': 'Sul', 'estado': 'vigente', 'texto': 'Na unidade Sul, a retirada exige agendamento.', 'vetor': [0, 1]},
            {'id': 'N-agenda', 'unidade': 'Norte', 'estado': 'vigente', 'texto': 'Na unidade Norte, a retirada não exige agendamento.', 'vetor': [0.6, 0.8]},
            {'id': 'N-frete', 'unidade': 'Norte', 'estado': 'vigente', 'texto': 'O frete depende do endereço de entrega.', 'vetor': [1, 0]}]}}

if __name__ == '__main__':
    p = Path(__file__).with_name('casos.json')
    p.write_text(json.dumps(dados(), ensure_ascii=False, indent=2)+'\n')
    print('casos.json: 2 consultas, 6 trechos fictícios, vetores fixos; sem semente aleatória (não se aplica).')
