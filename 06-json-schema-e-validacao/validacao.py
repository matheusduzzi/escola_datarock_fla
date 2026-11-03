"""Demonstração offline. Nenhum provedor ou modelo é chamado."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator


def sem_constante(valor):
    raise ValueError("constante fora de JSON")


def sem_duplicatas(pares):
    resultado = {}
    for chave, valor in pares:
        if chave in resultado:
            raise ValueError("chave duplicada")
        resultado[chave] = valor
    return resultado


def ler_json(texto):
    # Política local: texto limitado, sem cercas Markdown, constantes ou chaves repetidas.
    if not isinstance(texto, str) or len(texto.encode("utf-8")) > 10000:
        raise ValueError("texto ausente ou acima do limite didático")
    return json.loads(texto, parse_constant=sem_constante, object_pairs_hook=sem_duplicatas)


SCHEMA = json.loads(Path(__file__).with_name("schema-demo.json").read_text())
Draft202012Validator.check_schema(SCHEMA)
VALIDADOR = Draft202012Validator(SCHEMA)


def validar(texto):
    try:
        dado = ler_json(texto)
    except (ValueError, RecursionError):
        return {"ok": False, "etapa": "leitura", "erros": ["json_invalido"]}
    erros = [{"caminho": list(e.absolute_path), "regra": e.validator}
             for e in VALIDADOR.iter_errors(dado)]
    erros.sort(key=lambda e: (str(e["caminho"]), e["regra"]))
    if erros:
        return {"ok": False, "etapa": "schema", "erros": erros}
    return {"ok": True, "etapa": "schema", "dado": dado}


if __name__ == "__main__":
    casos = json.loads(Path(__file__).with_name("dados").joinpath("respostas.json").read_text())
    for caso in casos:
        r = validar(caso["texto"])
        print(caso["id"] + ": " + ("aceita" if r["ok"] else "rejeita/" + r["etapa"]))
