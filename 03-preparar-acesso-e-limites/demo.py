"""Rode dentro da pasta dessa aula: python3 -B demo.py"""
import json
import sys
from pathlib import Path
from limites import Config, Sessao, modelo_fixo


def main():
    if sys.version_info < (3, 9):
        raise SystemExit('Use Python 3.9 ou superior.')
    pasta = Path(__file__).resolve().parent
    config = Config(**json.loads((pasta/'dados/config-demo.json').read_text()))
    s = Sessao(config, modelo_fixo)
    print(json.dumps(dict(python='.'.join(map(str, sys.version_info[:3])),
                         dependencias='biblioteca padrao', rede=False,
                         credenciais_lidas=False), ensure_ascii=False))
    for entrada in ['Consultar regra fictícia.', 'Repetir consulta fictícia.']:
        print(json.dumps(s.executar(entrada), ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    main()
