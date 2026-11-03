"""Casos fictícios fixos; sem sorteio ou dados reais. Gerar novamente preserva os bytes."""
from pathlib import Path
import json
P = Path(__file__).resolve().parent
base = {"pedido": 1042, "status": "enviado", "prazo_dias": 7, "fonte": "politica-v1"}
def texto(**mudancas):
    return json.dumps(dict(base, **mudancas), ensure_ascii=False, sort_keys=True)
casos = [
    ("boa", texto()),
    ("aspas_simples", str(base)),
    ("cerca_markdown", "```json\n" + texto() + "\n```"),
    ("tipo_texto", texto(prazo_dias="7")),
    ("booleano", texto(prazo_dias=True)),
    ("campo_extra", texto(email="nao-usar")),
    ("enum", texto(status="a caminho")),
    ("negativo", texto(prazo_dias=-1)),
    ("acima_limite", texto(prazo_dias=31)),
    ("ausente", json.dumps({k:v for k,v in base.items() if k != "fonte"}, sort_keys=True)),
    ("nulo", texto(fonte=None)),
    ("lista", "[]"),
    ("fracionario", texto(prazo_dias=7.5)),
    ("inteiro_decimal", texto(prazo_dias=7.0)),
    ("duplicata", '{"pedido":1042,"pedido":1043}'),
    ("constante", texto().replace('7', 'NaN')),
    ("silenciosa", texto(prazo_dias=30))]
(P/"respostas.json").write_text(json.dumps([{"id":i,"texto":t} for i,t in casos],ensure_ascii=False,indent=2)+"\n")
(P/"politica.json").write_text(json.dumps({"id":"politica-v1","prazo_dias":7,"descricao":"Prazo fictício do caso, sem relação com política comercial real."},ensure_ascii=False,indent=2)+"\n")
print("Gerados 17 casos fixos e 1 política fictícia; sem aleatoriedade.")
