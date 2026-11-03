"""Inspeção de campos fictícios. Não classifica texto livre nem chama modelo."""
from pathlib import Path
import json

def inspecionar():
    dados = json.loads((Path(__file__).parent/'dados/demonstracao.json').read_text())
    for r in dados['respostas']:
        assert set(r) == {'id','prazo','unidade','condicao','fonte'}
        assert type(r['prazo']) is int
        assert all(isinstance(r[k],str) for k in ('id','unidade','condicao','fonte'))
        print(f"{r['id']}: estrutura=ok; prazo={r['prazo']}; unidade={r['unidade']}; condição={r['condicao']}; fonte={r['fonte']}")

if __name__ == '__main__':
    inspecionar()
