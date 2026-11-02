"""Rode dentro da pasta dessa aula: python3 -B guiada.py"""
import json
from limites import Config, Sessao, modelo_fixo

config = Config(max_tentativas=2, max_entrada_chars=200, max_saida_chars=80,
                orcamento_unidades=10, reserva_unidades=6)
s = Sessao(config, modelo_fixo)
for entrada in ['Consultar regra.', 'Repetir a consulta.']:
    print(json.dumps(s.executar(entrada), ensure_ascii=False, sort_keys=True))
