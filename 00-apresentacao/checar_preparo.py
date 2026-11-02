"""Inspeção de entrada, sem rede e sem resposta do diagnóstico."""
import json
import pathlib
import platform

def ler():
    caminho = pathlib.Path(__file__).resolve().parent / 'dados' / 'registros.json'
    registros = json.loads(caminho.read_text(encoding='utf-8'))
    if not isinstance(registros, list) or not registros:
        raise ValueError('Esperada lista não vazia')
    for r in registros:
        if not isinstance(r, dict) or set(r) != {'id', 'ativo'}:
            raise ValueError('Campos inválidos')
        if not isinstance(r['id'], str) or type(r['ativo']) is not bool:
            raise ValueError('Tipos inválidos')
    return registros

if __name__ == '__main__':
    registros = ler()
    print('Python:', platform.python_version())
    print('Entrada fictícia lida; registros:', len(registros))
    print('Campos: id (texto), ativo (booleano)')
    print('Sem rede. Resolva as tarefas em exercicios/diagnostico.md.')
