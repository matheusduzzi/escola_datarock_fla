"""Fixtures sintéticas, sem rede, sem aleatoriedade e sem credenciais."""
import json
from pathlib import Path
P = Path(__file__).resolve().parent / 'dados'

def gerar():
    pedido = {'model': 'modelo-demo-ficticio', 'instructions': 'Responda usando apenas a regra fornecida.', 'input': 'Na Loja Farol fictícia, a troca é permitida em 7 dias. Qual é o prazo?', 'max_output_tokens': 64, 'store': False}
    def caso(nome, http, corpo):
        return dict(caso=nome, origem='sintetica', pedido=pedido.copy(), http_status=http, corpo=corpo)
    def resposta(status, texto, uso, motivo=None):
        return dict(id='resp_demo', model='modelo-demo-ficticio', status=status, output=[{'type':'reasoning'}, {'type':'message', 'content':[{'type':'output_text','text':texto}]}], usage=uso, incomplete_details={'reason':motivo} if motivo else None, error=None)
    def erro(codigo, tipo):
        return {'error': {'code':codigo, 'type':tipo, 'message':'Mensagem sintética omitida do registro compartilhável.'}}
    casos = [caso('sucesso',200,resposta('completed','O prazo é de 7 dias.',dict(input_tokens=30,output_tokens=9,total_tokens=39))),
             caso('incompleta',200,resposta('incomplete','O prazo é',dict(input_tokens=30,output_tokens=4,total_tokens=34),'max_output_tokens')),
             caso('autenticacao',401,erro('invalid_api_key','invalid_request_error')),
             caso('limite_taxa',429,erro('rate_limit_exceeded','rate_limit_error')),
             caso('cota',429,erro('credit_balance_exhausted','insufficient_quota')),
             caso('servidor',503,erro('server_error','server_error')),
             caso('timeout',None,None), caso('json_invalido',200,'isto nao e JSON')]
    casos[1]['pedido']['max_output_tokens'] = 4
    P.mkdir(exist_ok=True)
    (P/'casos.json').write_text(json.dumps(casos,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Gerados 8 casos sintéticos; semente: não aplicável (literais fixos). Rede: não usada.')
if __name__ == '__main__': gerar()
