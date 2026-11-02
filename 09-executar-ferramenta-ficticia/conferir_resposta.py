"""Exemplos públicos do contrato; não contém implementação do exercício."""
import importlib.util
from pathlib import Path
import sys
from laco import ModeloRoteiro, rodar


def conferir(executor):
    assert executor('consultar_estoque','{"sku":"CX-02"}') == (
        {'ok':True,'sku':'CX-02','quantidade':0}, True)
    assert executor('consultar_estoque','{"sku":false}') == (
        {'ok':False,'erro':'argumentos_invalidos'}, False)
    assert executor('gravar_estoque','{}') == (
        {'ok':False,'erro':'ferramenta_nao_permitida'}, False)
    pedidos = [dict(tipo='ferramenta',id=str(i),nome='consultar_estoque',
                    argumentos='{"sku":false}') for i in range(4)]
    m=ModeloRoteiro(pedidos)
    r=rodar(m,3,executor)
    assert (r['fim'],r['tentativas'],r['execucoes']) == ('limite_de_passos',3,0)
    assert len(m.recebidos) == 3
    return 'Contrato público: zero, tipo inválido, nome proibido e teto conferidos.'


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Uso: python3 -B conferir_resposta.py resposta.py')
    spec=importlib.util.spec_from_file_location('resposta',Path(sys.argv[1]).resolve())
    modulo=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    print(conferir(modulo.executar_estoque))
