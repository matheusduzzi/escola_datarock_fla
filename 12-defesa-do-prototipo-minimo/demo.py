"""Executa fixtures autorais, sem rede, sem credenciais, sem aleatoriedade."""
import json
from pathlib import Path
from laco import ModeloRoteiro, rodar
from custos import custo


def chamada(nome='consultar_pedido', args='{"id_pedido":1042}', id='c1'):
    return dict(tipo='ferramenta', id=id, nome=nome, argumentos=args)


def demonstrar():
    cenarios = {
        'consulta': [chamada(), dict(tipo='texto', texto='Pedido 1042: separando.')],
        'acao_negada': [chamada(nome='cancelar_pedido'), dict(tipo='texto', texto='Ação não permitida.')],
        'json_invalido': [chamada(args='{'), dict(tipo='texto', texto='Solicitar correção.')],
        'repeticao': [chamada(id=str(i)) for i in range(4)],
    }
    registros = {}
    for nome, respostas in cenarios.items():
        modelo = ModeloRoteiro(respostas)
        r = rodar(modelo, max_passos=3)
        registros[nome] = r
        print('{}: fim={} passos={} tentativas={} execucoes={}'.format(
            nome, r['fim'], r['passos'], r['tentativas'], r['execucoes']))
    usos = [{'entrada':30,'saida':8}, {'entrada':50,'saida':10}]
    valor = custo(usos)
    print('Uso SINTÉTICO da consulta: entrada=80 saida=18')
    print('Custo didático R$ {:.6f}; 1000 consultas iguais R$ {:.6f}'.format(valor,valor*1000))
    print('Sem usage: custo={}; chamada real=não realizada; latência real=não medida'.format(custo([None])))
    return {'modo':'offline_sintetico_v1', 'cenarios':registros, 'uso_consulta':usos,
            'custo_ficticio_rs':str(valor), 'chamada_real':False, 'latencia_real_ms':None}


if __name__ == '__main__':
    demonstrar()
