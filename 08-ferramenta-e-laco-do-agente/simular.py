"""Laço didático offline. Não chama API, não mede modelo real."""
import json
from pathlib import Path


def rodar(respostas, max_passos=3, autorizados=(1042,)):
    """Um passo = uma resposta programada; no máximo uma ferramenta por passo."""
    if type(max_passos) is not int or max_passos < 1:
        raise ValueError('max_passos deve ser inteiro positivo')
    historico, eventos = [], []
    execucoes = 0
    for passo in range(1, max_passos + 1):
        if passo > len(respostas):
            return dict(fim='roteiro_esgotado', passos=passo-1,
                        execucoes=execucoes, eventos=eventos, historico=historico)
        r = respostas[passo-1]
        historico.append(dict(papel='modelo', conteudo=r))
        eventos.append(dict(passo=passo, evento='modelo', tipo=r.get('tipo')))
        if r.get('tipo') == 'texto':
            return dict(fim='resposta', passos=passo, execucoes=execucoes,
                        texto=r.get('texto', ''), eventos=eventos, historico=historico)
        if r.get('tipo') != 'ferramenta':
            return dict(fim='pedido_malformado', passos=passo, execucoes=execucoes,
                        eventos=eventos, historico=historico)
        nome, args = r.get('nome'), r.get('argumentos')
        if nome != 'consultar_pedido':
            resultado = dict(ok=False, erro='ferramenta_nao_permitida')
        elif (type(args) is not dict or set(args) != {'id_pedido'}
              or type(args['id_pedido']) is not int or args['id_pedido'] < 1):
            resultado = dict(ok=False, erro='argumentos_invalidos')
        elif args['id_pedido'] not in autorizados:
            resultado = dict(ok=False, erro='acesso_negado')
        else:
            # Somente este ramo representa a execução da ferramenta fictícia.
            execucoes += 1
            resultado = dict(ok=True, id_pedido=args['id_pedido'], status='separando')
        eventos.append(dict(passo=passo, evento='resultado', **resultado))
        historico.append(dict(papel='ferramenta', conteudo=resultado))
    return dict(fim='limite_de_passos', passos=max_passos, execucoes=execucoes,
                eventos=eventos, historico=historico)


def demonstrar():
    dados = json.loads((Path(__file__).parent/'dados/casos.json').read_text())
    return {nome: rodar(respostas) for nome, respostas in dados.items()}


if __name__ == '__main__':
    print(json.dumps(demonstrar(), ensure_ascii=False, indent=2))
