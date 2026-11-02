"""Laboratório offline FLA R09, Python 3.9+, somente biblioteca padrão."""
from copy import deepcopy
import json
from pathlib import Path


def sem_duplicatas(pares):
    objeto = {}
    for chave, valor in pares:
        if chave in objeto:
            raise ValueError('chave duplicada')
        objeto[chave] = valor
    return objeto


def ler_argumentos(texto):
    if type(texto) is not str or len(texto) > 512:
        raise ValueError('argumentos devem ser JSON curto')
    return json.loads(texto, object_pairs_hook=sem_duplicatas)


def consultar_pedido(id_pedido):
    pedidos = json.loads((Path(__file__).parent/'dados/pedidos.json').read_text())
    pedido = pedidos.get(str(id_pedido))
    if pedido is None:
        return {'ok': False, 'erro': 'pedido_nao_encontrado'}
    return {'ok': True, 'pedido': {'id_pedido': id_pedido, **pedido}}


def executar(nome, texto, consulta=consultar_pedido):
    """Retorna (resultado, executou). Só aceita a ferramenta de leitura prevista."""
    if nome != 'consultar_pedido':
        return {'ok': False, 'erro': 'ferramenta_nao_permitida'}, False
    try:
        args = ler_argumentos(texto)
    except (ValueError, RecursionError):
        return {'ok': False, 'erro': 'json_invalido'}, False
    if (type(args) is not dict or set(args) != {'id_pedido'}
            or type(args['id_pedido']) is not int or args['id_pedido'] <= 0):
        return {'ok': False, 'erro': 'argumentos_invalidos'}, False
    # Política fictícia da sessão, definida pelo código e não pelo modelo.
    if args['id_pedido'] not in (1042, 1043, 9999):
        return {'ok': False, 'erro': 'acesso_negado'}, False
    try:
        return consulta(args['id_pedido']), True
    except Exception:
        return {'ok': False, 'erro': 'falha_ferramenta'}, True


class ModeloRoteiro:
    """Substituto programado; guarda o que recebeu antes de cada resposta."""
    def __init__(self, respostas):
        self.respostas = deepcopy(respostas)
        self.recebidos = []

    def responder(self, mensagens):
        if len(self.recebidos) >= len(self.respostas):
            raise StopIteration
        self.recebidos.append(deepcopy(mensagens))
        return deepcopy(self.respostas[len(self.recebidos)-1])


def rodar(modelo, max_passos=3, executor=executar):
    """Um passo inclui uma resposta do modelo e, se pedida, uma tentativa de ferramenta.

    Envelope local, sem compatibilidade prometida com SDK/protocolo externo.
    executor é código confiável. Erros de programação nele não são ocultados.
    """
    if type(max_passos) is not int or not 1 <= max_passos <= 20:
        raise ValueError('max_passos deve ser inteiro de 1 a 20')
    mensagens, ids = [], set()
    tentativas = execucoes = passos = 0

    def terminar(fim):
        return dict(fim=fim, passos=passos, tentativas=tentativas,
                    execucoes=execucoes, mensagens=deepcopy(mensagens))

    for passos in range(1, max_passos+1):
        try:
            resposta = modelo.responder(deepcopy(mensagens))
        except StopIteration:
            passos -= 1
            return terminar('roteiro_esgotado')
        mensagens.append({'papel': 'modelo', 'conteudo': deepcopy(resposta)})
        if (type(resposta) is dict and set(resposta) == {'tipo', 'texto'}
                and resposta['tipo'] == 'texto' and type(resposta['texto']) is str):
            return terminar('resposta')
        if (type(resposta) is not dict
                or set(resposta) != {'tipo', 'id', 'nome', 'argumentos'}
                or resposta['tipo'] != 'ferramenta'
                or type(resposta['nome']) is not str
                or type(resposta['id']) is not str or not resposta['id']
                or resposta['id'] in ids):
            return terminar('pedido_malformado')
        ids.add(resposta['id'])
        tentativas += 1  # Inclui JSON inválido, nome negado e erro da ferramenta.
        resultado, executou = executor(resposta['nome'], resposta['argumentos'])
        execucoes += int(executou)
        mensagens.append({'papel': 'ferramenta', 'id': resposta['id'],
                          'conteudo': deepcopy(resultado)})
    return terminar('limite_de_passos')
