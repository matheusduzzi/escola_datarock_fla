"""Contrato público: executa a função entregue pelo aluno, sem incluir implementação."""
import argparse
import importlib.util
import json
from pathlib import Path
from inspecionar import inspecionar

def testar(funcao):
    casos=json.loads((Path(__file__).resolve().parent/'dados/casos.json').read_text())
    esperado={'cota':'revisar_saldo','limite_taxa':'aguardar_com_limite','json_invalido':'investigar_corpo'}
    for caso in casos:
        if caso['caso'] in esperado:
            assert funcao(inspecionar(caso))==esperado[caso['caso']], caso['caso']
    assert funcao({'erro':'erro_nao_catalogado','http_status':429,'uso':None})=='revisao_humana'
    assert funcao({'erro':None,'http_status':200,'uso':None})=='revisao_humana'
    print('Contrato da decisão: 5 casos passaram. Nenhuma chamada real.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--modulo',type=Path,required=True)
    args=parser.parse_args(); spec=importlib.util.spec_from_file_location('aluno',args.modulo)
    modulo=importlib.util.module_from_spec(spec); spec.loader.exec_module(modulo)
    testar(modulo.decidir)
