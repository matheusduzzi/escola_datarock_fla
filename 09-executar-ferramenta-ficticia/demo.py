"""Executa as respostas fixas, sem rede, API ou credencial."""
import json
from pathlib import Path
from laco import ModeloRoteiro, rodar

if __name__ == '__main__':
    casos = json.loads((Path(__file__).parent/'dados/casos.json').read_text())
    saida = {}
    for nome, respostas in casos.items():
        modelo = ModeloRoteiro(respostas)
        saida[nome] = {'resultado': rodar(modelo), 'recebidos': modelo.recebidos}
    print(json.dumps(saida, ensure_ascii=False, indent=2))
