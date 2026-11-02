"""Montador didático offline. Não implementa protocolo de provedor nem chama modelo."""
from copy import deepcopy
import json
from pathlib import Path

INSTRUCAO = {"id": "i", "papel": "instrucao", "texto": "Responda só com fatos presentes no pedido. Se faltar evidência, peça confirmação."}

def montar(estado, conversa, atual, limite, usar_memoria=False):
    if estado["conversa"] != conversa:
        raise ValueError("conversa divergente")
    if isinstance(limite, bool) or not isinstance(limite, int) or limite < 1:
        raise ValueError("limite deve ser inteiro positivo")
    candidatos = deepcopy(estado["historico"]) + [deepcopy(atual)]
    escolhidos = candidatos[-limite:]
    omitidos = candidatos[:-limite]
    memoria = deepcopy(estado.get("memoria", [])) if usar_memoria else []
    return {"conversa": conversa, "instrucao": deepcopy(INSTRUCAO),
            "memoria_incluida": memoria, "mensagens": escolhidos,
            "omitidos": [{"id": m["id"], "motivo": "fora da seleção didática"} for m in omitidos],
            "limite_mensagens": limite}

def salvar(estado, caminho):
    Path(caminho).write_text(json.dumps(estado, ensure_ascii=False, indent=2)+"\n")

def carregar(caminho):
    return json.loads(Path(caminho).read_text())
