"""Reproduz fixtures autorais; não chama modelo nem usa rede."""
import json
from pathlib import Path
DADOS = Path(__file__).resolve().parent / 'dados'

def repetir():
    return json.loads((DADOS / 'saidas.json').read_text())

if __name__ == '__main__':
    print(json.dumps(repetir(), ensure_ascii=False, indent=2))
