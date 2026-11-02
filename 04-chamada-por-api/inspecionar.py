"""Leitor offline de envelopes didáticos. Não é cliente HTTP nem filtro universal de segredos."""
import argparse
import hashlib
import json
from pathlib import Path

CODIGOS = {'invalid_api_key','rate_limit_exceeded','credit_balance_exhausted','server_error'}
ESTADOS = {'completed','incomplete','failed','in_progress','queued','cancelled'}

def digest(valor):
    return hashlib.sha256(json.dumps(valor,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def inspecionar(caso):
    """Só persiste campos numéricos ou categorias fechadas; conteúdo livre fica de fora."""
    pedido = caso['pedido']
    http = caso.get('http_status')
    if http is not None and (type(http) is not int or not 100 <= http <= 599):
        raise ValueError('http_status inválido')
    registro = dict(modo='offline_sintetico', pedido_sha256=digest(pedido), http_status=http,
                    estado=None, erro=None, motivo_incompleta=None, uso=None, partes_texto=0,
                    limite_saida=pedido.get('max_output_tokens') if type(pedido.get('max_output_tokens')) is int else None)
    if http is None:
        registro['erro']='timeout_simulado'
        return registro
    corpo = caso.get('corpo')
    if not isinstance(corpo,dict):
        registro['erro']='corpo_invalido'
        return registro
    erro = corpo.get('error')
    if isinstance(erro,dict):
        codigo = erro.get('code')
        registro['erro']=codigo if isinstance(codigo,str) and codigo in CODIGOS else 'erro_nao_catalogado'
    estado = corpo.get('status')
    registro['estado'] = estado if isinstance(estado,str) and estado in ESTADOS else None
    if http >= 400:
        registro['erro'] = registro['erro'] or 'erro_http_nao_catalogado'
        return registro
    uso = corpo.get('usage')
    if isinstance(uso,dict):
        valores = {k:uso.get(k) for k in ('input_tokens','output_tokens','total_tokens')}
        if all(type(v) is int and v >= 0 for v in valores.values()) and valores['total_tokens']==valores['input_tokens']+valores['output_tokens']:
            registro['uso']=valores
        else:
            registro['erro']=registro['erro'] or 'uso_invalido'
    detalhes = corpo.get('incomplete_details')
    if isinstance(detalhes,dict):
        motivo=detalhes.get('reason')
        registro['motivo_incompleta']=motivo if motivo in ('max_output_tokens','content_filter') else 'outro'
    itens = corpo.get('output')
    if isinstance(itens,list):
        for item in itens:
            if not isinstance(item,dict) or item.get('type') != 'message': continue
            conteudo = item.get('content')
            if not isinstance(conteudo,list): continue
            for parte in conteudo:
                if isinstance(parte,dict) and parte.get('type')=='output_text' and isinstance(parte.get('text'),str) and parte['text'].strip():
                    registro['partes_texto'] += 1
    return registro

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--caso',default='todos')
    parser.add_argument('--saida',type=Path,required=True)
    args=parser.parse_args()
    casos=json.loads((Path(__file__).resolve().parent/'dados/casos.json').read_text(encoding='utf-8'))
    casos=[c for c in casos if args.caso=='todos' or c['caso']==args.caso]
    if not casos: parser.error('caso desconhecido')
    args.saida.parent.mkdir(parents=True,exist_ok=True)
    linhas=[]
    for caso in casos:
        registro=inspecionar(caso)
        linhas.append(json.dumps(registro,ensure_ascii=False,sort_keys=True))
        uso=registro['uso']
        print('{}: http={} estado={} erro={} uso={} partes={}'.format(caso['caso'],registro['http_status'],registro['estado'],registro['erro'],uso['total_tokens'] if uso else 'desconhecido',registro['partes_texto']))
    args.saida.write_text('\n'.join(linhas)+'\n',encoding='utf-8')
    print('Registro salvo; rede=False; credenciais_lidas=False; custo_real=não medido.')
if __name__=='__main__': main()
